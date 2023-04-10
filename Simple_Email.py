from email.message import EmailMessage
import ssl
import smtplib
Email = "<your email>"
password = "<your password>"

email_receiver = "lodol14104@jthoven.com"

subject = "Just saying hello"
body = "Hello My Friend"

em = EmailMessage()
em["From"] = Email
em["To"] = email_receiver
em["Subject"] = subject
em.get_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as smtp:
    smtp.login(Email, password)
    smtp.sendmail(Email, email_receiver, em.as_string())