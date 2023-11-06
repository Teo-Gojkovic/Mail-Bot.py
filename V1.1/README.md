# Programme d'automatisation d'envois de mails en Python

![Version programme](https://img.shields.io/badge/Version-v1.1-blue.svg)
![Version python](https://img.shields.io/badge/Python-3.11.5-blue.svg)

Ce programme Python vous permet d'automatiser l'envoi de mails à une liste de destinataires spécifiée dans un dictionnaire Python. Vous pouvez également inclure des pièces jointes provenant d'un répertoire nommé "fichiers".

## Fonctionnalités

- Envoi de mails en masse à une liste de destinataires définie dans un fichier excel.
- Inclusion de pièces jointes depuis le répertoire "fichiers".
- Mail plus ou moins personnalisé

## Prérequis

1. [Python 3.11](https://www.python.org/downloads/release/python-3110/)

2. [Smtplib](https://pypi.org/project/secure-smtplib/)

3. IDE comme : [VS Code](https://code.visualstudio.com) / [PyCharm](https://www.jetbrains.com/fr-fr/pycharm/) / [Spyder](https://www.spyder-ide.org)

4. Utilisez le fichier excel fourni : "**liste-email.xlsx**"

## Configuration

### 1 - Il faudra compléter les variables, elles ne sont pas toutes obligatoires :

```py
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
```

### 2 - Contenu du mail : 

```py
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
```

### 3 - Connection au serveur SMTP :
Cette partie du code, il ne faut pas à modifier, il faut simplement choisir votre serveur SMTP (Google/OVH/Free ect...)

Si vous ne le connaissez pas : https://www.pc83.fr/tools/liste-des-serveurs-mails-orange-sfr-free.html

Si vous utilisez Gmail ou OVH, vous devez simplement modifier ce boolean :

```py
choix_smtp = True # True = OVH / False = Google Gmail
```

### 4 - Fichier excel :
Dans le fichier excel : "**liste-email.xlsx**"

| nom | email | pj1 | pj2 | pj3 |
|:----------:|:----------:|:----------:|:----------:|:----------:|
| Nom 1 | exemple1@gmail.com | cv.png | lettre-motivation1.png | |
| Nom 2 | exemple2@gmail.com | cv.png | lettre-motivation2.png | |
| Nom 3 | exemple3@gmail.com | cv.png | lettre-motivation3.png | |

Vous n'êtes pas obligé de remplir les colonnes ***pj*** si elles sont vides il faudra simplement modifier légèrement le code :
```py
    nom_fichier_1 = row['pj1']
    nom_fichier_2 = row['pj2']
    #nom_fichier_3 = row['pj3']  
```

Vous devez mettre ou enlever le commentaire "**#**".

Il faudra bien penser à aussi changer cette ligne :

```py
attachment_paths = [f"fichiers/{nom_fichier_1}", f"fichiers/{nom_fichier_2}"]
```

**N'oubliez pas la virgule**

## Documentation

- [smtplib](https://docs.python.org/3/library/smtplib.html)
- [time](https://docs.python.org/3/library/time.html)
- [pandas](https://pandas.pydata.org/docs/user_guide/index.html)

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Auteur

[![Teo GOJKOVIC](https://img.shields.io/badge/Teo_GOJKOVIC-222e45?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Teo-Gojkovic)