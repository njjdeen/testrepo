import smtplib
import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)

smtp_object.ehlo()

smtp_object.starttls()

#input("What is your password: ")
email = getpass.getpass('Email:')
password = getpass.getpass('Password please:')


smtp_object.login(email,password)

for i in range(0,10):
    from_address = email
    to_address = 'lex.koning@devoteam.com'
    subject =  "Lekkers"
    message = "Gaal Lekker"
    
    
    msg = "Subject: "+subject+'\n'+message
    
    smtp_object.sendmail(from_address,to_address,msg)

smtp_object.quit()