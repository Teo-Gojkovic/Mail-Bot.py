# Programme d'automatisation d'envoi de mails en Python

![Version programme](https://img.shields.io/badge/Version-v1.1-blue.svg)
![Version python](https://img.shields.io/badge/Python-3.11.5-blue.svg)

Ce programme Python vous permet d'automatiser l'envoi de mails à une liste de destinataires spécifiée dans un dictionnaire Python. Vous pouvez également inclure des pièces jointes provenant d'un répertoire nommé "fichiers".

## Fonctionnalités

- Envoi de mails en masse à une liste de destinataires défini dans un fichier excel.
- Inclusion de pièces jointes depuis le répertoire "fichiers".
- Mail plus ou moins personalisé par email

## Prérequis

1. [Python 3.11](https://www.python.org/downloads/release/python-3110/)

2. [Smtplib](https://pypi.org/project/secure-smtplib/)

3. IDE comme : [VS Code](https://code.visualstudio.com) / [PyCharm](https://www.jetbrains.com/fr-fr/pycharm/) / [Spyder](https://www.spyder-ide.org)

## Configuration

### 1 - Il faudra completer les variables, elle ne sont pas toute obligatoire : 

```py
# ------------------------------ Variables ------------------------------ 
# Configurations d'envoi d'e-mails - OBLIGATOIRE
sender_email = ""       # Entrez votre adresse email
sender_password = ""    # Entrez votre mot de passe
subject = ""            # Entrez l'objet de votre email

# Coordonnées pour le contenu du mail : 
nom = ""                # Entrez votre nom de famille en MAJUSCULE
prenom = ""             # Entrez votre prénom
mail = ""               # Entrez votre email principal / pro
numero = ""             # Entrez votre numéro de téléphone
linkedin = ""           # Entrez le lien de votre page linkedin
github = ""             # Entrez le lien de votre github
```

### 2 - Contenu du mail : 

```py
# Contenu du mail
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
Cette partie du code il ne faut pas a modifier, il faut simplment choisir votre serveur SMTP (Google / OVH / Free ect...)

Si vous le connaisez pas : https://www.pc83.fr/tools/liste-des-serveurs-mails-orange-sfr-free.html

Si vous utiliser Gmail ou OVH vous devez simplement modifier ce boolean : 

```py
choix_smtp = True # True = OVH / False = Google Gmail
```

### 4 - Fichier excel :
Dans le fichier excel "**liste-email.xlsx**" 

Dans la fin du programme il faudra modifier le nombre de pieces jointes :

```py
attachment_paths = [f"fichiers/{nom_fichier_1}", f"fichiers/{nom_fichier_2}"]
```

Dans le cas ou vous avez plus de pieces jointes il faudra simplement les ajouter a la suite ex :

```py
attachment_paths = [f"fichiers/{nom_fichier_1}", f"fichiers/{nom_fichier_2}", f"fichiers{nom_fichier_3}"]
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