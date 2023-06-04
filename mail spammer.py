import yagmail
import time

print("Welcome!")
# Mail sender account

mail = input("Please enter mail sender account(example:hola39799@gmail.com): ")
apppassword = input("Please enter app password for mail provided: ")

yag = yagmail.SMTP(user=mail, password=apppassword)

destinatario = input("receiver mail: ")
asunto = input("Affair: ")
mensaje = input("Message: ")
num = input("How many mails send?: ")
num = int(num)
for x in range(num):
    yag.send(destinatario, asunto, mensaje)
    time.sleep(1)
    print("finalizado")