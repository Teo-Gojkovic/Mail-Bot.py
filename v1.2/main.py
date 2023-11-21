import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time
import pandas as pd

# ------------------------------ Feuille excel ------------------------------
df_mail = pd.read_excel('data.xlsx', sheet_name='liste-email') ; df_mail.head()
df_var = pd.read_excel('data.xlsx', sheet_name='variables', header=None, names=['Variable', 'Valeur']) ; df_var.head()

#déclaration des variables dans un dictionaire.
variables = dict(zip(df_var['Variable'], df_var['Valeur']))

# ------------------------------ Email ------------------------------
# Configurations d'envoi d'e-mails - OBLIGATOIRE
sender_email = ""       # Entrez votre adresse email
sender_password = ""    # Entrez votre mot de passe
subject = ""            # Entrez l'objet de votre email

# Ouverture de email.txt
with open('email.txt', 'r', encoding='utf-8') as file:
    email = file.read()
message = email.format(**variables) #intégration des variables dans le message du mail.

# ------------------------------ Connection au serveur SMTP ------------------------------
# Choix SMTP config : 
# Gmail config : 
gmail_smtp_server = "smtp-relay.gmail.com"
gmail_smtp_port = 587

# OVH config : 
OVH_smtp_server = "ssl0.ovh.net"
OVH_smtp_port = 465

choix_smtp = True # True = OVH / False = Google Gmail

if choix_smtp == True : 
    smtp_server = OVH_smtp_server
    smtp_port = OVH_smtp_port
else : 
    smtp_server = gmail_smtp_server
    smtp_port = gmail_smtp_port

print("CONNECTION AU SERVEUR EN COURS ...") ; print()
try : 
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.login(sender_email, sender_password)
    print("Connection établie !")
except : 
    print("La connexion au serveur SMTP a échoué")  

# ------------------------------ Fonctions ------------------------------
def send_email(sender_email, sender_password, receiver_email, subject, message, attachment_path):
    start_time = time.time()  
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))
    try : 
        for attachment_path in attachment_paths:
            attachment = open(attachment_path, "rb")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % attachment_path)
            msg.attach(part)
    
    except : 
        print("pas de pièce-jointe.")

    server.sendmail(sender_email, receiver_email, msg.as_string())
    
    end_time = time.time()
    elapsed_time = end_time - start_time  

    print(f"Email pour {nom_liste} a été envoyé en {elapsed_time:.2f} secondes.") 

# Envoi de mail.
for index, row in df_mail.iterrows():
    adresse_email = row['email']
    nom_liste = row['nom']
    nom_fichier_1 = row['pj1']
    nom_fichier_2 = row['pj2']
    #nom_fichier_3 = row['pj3']

    attachment_paths = [f"fichiers/{nom_fichier_1}"]
    
    send_email(sender_email, sender_password, adresse_email, subject, message, attachment_paths)
    
server.quit()
print() ; print("Connexion au serveur SMTP coupé")