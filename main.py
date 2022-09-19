import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

listOfEmails = []

emailsData = input("Please enter the name of the file in which your emails are stored in: ")

file1 = open(emailsData, 'r')
totalines = file1.readlines()
for s in totalines:
     listOfEmails.append(s.strip() + "@gmail.com")
print(listOfEmails)

for i in listOfEmails:
    sender_email = "isai10morales@aol.com"
    receiver_email = i
    password = "fwtkjnqptlcrjlgs"
    
    message = MIMEMultipart("alternative")
    message["Subject"] = "Cashapp Signup Referral"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    html = """
      <!DOCTYPE html>
      <html>
          <head>
              <title>Example</title>
          </head>
          <body>
              <p>This is an example of a simple HTML page with one paragraph.</p>
          </body>
      </html>
    """

    # Turn these into plain/html MIMEText objects
    part2 = MIMEText(html, 'html')

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.aol.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

    time.sleep(60)
    print("[+] Succesfully sent email to " + i)
