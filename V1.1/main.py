import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time
import pandas as pd

# ------------------------------ Variables ------------------------------ 
# Coordonnées pour le contenu du mail : 
nom = ""                # Entrez votre nom de famille en MAJUSCULE
prenom = ""             # Entrez votre prénom
mail = ""               # Entrez votre email principal / pro
numero = ""             # Entrez votre numéro de téléphone
linkedin = ""           # Entrez le lien de votre page linkedin
github = ""             # Entrez le lien de votre github

# Configurations d'envoi d'e-mails - OBLIGATOIRE
sender_email = ""       # Entrez votre adresse email
sender_password = ""    # Entrez votre mot de passe
subject = ""            # Entrez l'objet de votre email
message = f""" 
Bonjour ceci est un mail d'exemple écrit par {prenom} {nom}.
Mes réseaux sont les suivant : 
    Linkedin : {linkedin}
    Github : {github}
    
Pour me contacter : 
Email : {mail}
N° téléphone : {numero}

Cordialement,
{nom} {prenom}
"""

df = pd.read_excel('liste-email.xlsx')

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

# ------------------------------ Feuille excel ------------------------------
workbook = pd.read_excel('liste-email.xlsx')
workbook.head()    

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
for index, row in df.iterrows():
    adresse_email = row['email']
    nom_liste = row['nom']
    nom_fichier_1 = row['pj1']
    #nom_fichier_2 = row['pj2']
    #nom_fichier_3 = row['pj3']

    attachment_paths = [f"fichiers/{nom_fichier_1}"]
    
    send_email(sender_email, sender_password, adresse_email, subject, message, attachment_paths)
    
server.quit()
print() ; print("Connexion au serveur SMTP coupé")