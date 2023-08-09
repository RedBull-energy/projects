from django.db import models


class Contact(models.Model):
    email_address = models.EmailField(max_length=150)
    username = models.CharField(max_length=50)
