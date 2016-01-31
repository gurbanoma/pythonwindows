#!C:/Python34/python.exe -u
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = 'g.urbano.ma@gmail.com'
toaddr = 'g.urbano.ma@gmail.com'
#me quede aqui bar si manda
text = 'test message sent from Python'
username = 'g.urbano.ma'
password = 'master18'
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Test'
msg.attach(MIMEText(text))
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.sendmail(fromaddr, toaddr, msg.as_string())
server.quit()
