#creating smtp library
#importing smtp library
import smtplib
#SMTP VIA GOOGLE
s=smtplib.SMTP('smtp.gmail.com',587)
#STARTING 
s.starttls()
#PROVIDIND THE SENDER EMAIL ID
s.login("syedafshana4812@gmail.com","nayeemunnisa123")
#WRITING THE MESSAGE
message="HEY SWATI HOW ARE YOU "
#sending a mail
s.sendmail("syedafshana4812@gmail.com","maniswati1999@gmail.com",message)
#terminating the sessions
s.quit()
