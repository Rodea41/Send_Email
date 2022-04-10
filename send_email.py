from email import message
import smtplib
import ssl
from email.message import EmailMessage
import login

subject = "Email from python"
body = "This is a test email from python"

#* Addresses are the same because I will be sending an email to myself
sender_email = login.email_address
receiver_email = login.email_address 
password = login.password

message = EmailMessage() # Instantiate an EmailMessage object and store in a variable

message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context() # Create a secure SSL context . This is needed for gmail to work/accept the email

print("Sending email!")


#* The code below connects to gmails stmp server through port 465 and uses a secure socket layer (SSL) that we
#* created in the code above.
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())


print("Email sent!")