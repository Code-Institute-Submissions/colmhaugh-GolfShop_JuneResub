from django.db import models


class Newsletter(models.Model):
    email = models.EmailField(null=False, blank=False, max_length=256)
    
