from Capstone_project import settings
from django.core.mail import send_mail


def send_email_notification(users,book):

    subject = f"{book.title} is now available"
    message = f" the book {book.title} is now available for checking out!"
    from_email = settings.DEFAULT_FROM_EMAIL
    for user in users:

        send_mail(subject,message,from_email,[user.email])
