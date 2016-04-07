

import yagmail #Import de la librairie yagmail

yag = yagmail.SMTP('emetteur@gmail.com', 'password') #Paramétrage du mail GMAIL emetteur et du mot de passe

contents = ['This is the body, and here is just text http://somedomain/image.png',
            'You can find an audio file attached.']
yag.send('j.serrand@icloud.com', 'Test Yagmail', contents)
