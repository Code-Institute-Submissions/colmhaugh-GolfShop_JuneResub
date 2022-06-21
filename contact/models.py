from django.db import models

class Contact(models.Model):
    email = models.EmailField(null=False, blank=False, max_length=256)
    name = models.CharField(null=False, blank=False, max_length=256)
    message = models.TextField(null=False, blank=False)