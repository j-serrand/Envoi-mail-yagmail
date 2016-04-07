# Envoi mail yagmail

Programme se basant sur la bibliothèque python créée par [Pascal Van Kooten](https://github.com/kootenpv), permettant à l'aide d'une configuration des plus simple d'envoyer un mail avec python à partir d'un compte GMAIL en utlisant SMTP.

## Installation de yagmail

La bibliothèque est disponible sur le [github de yagmail](https://github.com/kootenpv/yagmail), deux moyens s'offrent à vous pour l'exécuter :

* Mettre la bibliothèque dans le même dossier que le script python à éxecuter
* Installer la bibliothèque à l'aide du gestionnaire de paquets python : ``` pip install yagmail ```

## Utilisation de yagmail

### Paramétrage

``` python
import yagmail #Import de la librairie yagmail

yag = yagmail.SMTP('emetteur@gmail.com', 'password') #Paramétrage du mail GMAIL emetteur et du mot de passe
```

### Saisie d'un contenu et envoi d'un message

```python
contents = ['This is the body, and here is just text http://somedomain/image.png',
            'You can find an audio file attached.']

yag.send('envoi@test.com', 'Test Yagmail', contents) #Envoi du massage dont le contenu est dans contents
```

### A propos du paramétrage du port SMTP

Le port smtp utilisé pour l'envoi d'un message par yagmail peut être configuré dans le fichier ```yagmail\yagmail.py``` à la ligne 50 :

```python
def __init__(self, user=None, password=None, host='smtp.gmail.com',
                 port='587', smtp_starttls=True, smtp_set_debuglevel=0, smtp_skip_login=False,
                 **kwargs):
```

À l'origine le port est configuré sur 587. ***Si vous changez le port dans ce script il faut à tout prix que la bibliothèque yagmail avec le port modifié soit dans le même dossier que votre script.***

### Script de test
Un script de test python est fourni sur ce repository : [Envoi_mail_yagmail.py](Envoi_mail_yagmail.py)


 <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Licence Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Envoi mail yagmail</span> de <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Joris Serrand</span> est mis à disposition selon les termes de la <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">licence Creative Commons Attribution -  Partage dans les Mêmes Conditions 4.0 International</a>.