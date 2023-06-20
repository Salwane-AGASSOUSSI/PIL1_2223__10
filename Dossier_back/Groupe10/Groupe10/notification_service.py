from django.core.mail import EmailMessage

def send_notification_email(student_email, subject, message):
    email = EmailMessage(subject, message, to=[student_email])
    email.send()
