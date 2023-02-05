from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=56, name="contact_name")


class Numbers(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="numbers")
    phone_number = models.CharField(max_length=255)
