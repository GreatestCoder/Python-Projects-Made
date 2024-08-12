import smtplib
import ssl

def Emailer(message):
    username = "namansharma9858581009@gmail.com"
    password = "vbftlvruxkaeycvc"
    host = "smtp.gmail.com"
    port = 465
    receivers_email = "meteoritestudios123@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receivers_email, message)

