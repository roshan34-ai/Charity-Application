from django.utils.html import strip_tags
from django.contrib.sessions.backends.db import SessionStore
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from .models import *
import random, math

def send_email(name, email, contact_no, otp):
    html_content = render_to_string('charityapp/email1.html', {'name':name,
                                                            'email':email,
                                                            'otp':otp,
                                                            'contact_no':contact_no})
    text_content = strip_tags(html_content)
    email=email
    
    email = EmailMultiAlternatives(
                "User Varifivcation Mail",
                text_content,
                settings.EMAIL_HOST_USER,
                [email],
                )
    email.attach_alternative(html_content,"text/html")
    email.send()
    

def generateOTP() :
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    OTP = ""
    length = len(string)
    for i in range(6) :
        OTP += string[math.floor(random.random() * length)]
 
    return OTP