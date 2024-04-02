import smtplib
from email.message import EmailMessage


def send_text_email(receiver_email, subject, message):
    # Set up the email message
    email = EmailMessage()
    email["From"] = "pythondeveloper441@gmail.com"  # Sender's email address
    email["To"] = receiver_email  # Receiver's email address
    email["Subject"] = subject  # Subject of the email
    email.set_content(message)  # Body of the email

    # Connect to the SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()  # Start TLS encryption
        smtp.login(
            "pythondeveloper441@gmail.com", "$enterpassword$"
        )  # Login to the SMTP server
        smtp.send_message(email)  # Send the email


receiver_email = "abdusamaddev571@gmail.com"
subject = "Test Email"
message = "This is a test email sent from Python. manman, jala tushgan"
send_text_email(receiver_email, subject, message)
