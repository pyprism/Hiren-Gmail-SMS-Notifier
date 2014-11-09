from django.db import models
from django.contrib.auth.models import User


class Mail(models.Model):
    user = models.ForeignKey(User)
    mail_address = models.CharField(max_length=200)


class MailAuth(models.Model):
    mail = models.ForeignKey(Mail)
    authorization_code = models.CharField(max_length=200)
    refresh_token = models.CharField(max_length=200)


class Credential(models.Model):
    user = models.ForeignKey(User)
    twilio_account_sid = models.CharField(max_length=100)
    twilio_auth_token = models.CharField(max_length=100)
    twilio_phone_from = models.CharField(max_length=50)
    twilio_phone_to = models.CharField(max_length=50)


class Gmail(models.Model):
    client_id = models.CharField(max_length=100)
    client_secret = models.CharField(max_length=100)