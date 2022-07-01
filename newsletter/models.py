from django.db import models


class Newsletter(models.Model):
    email = models.EmailField(null=False, blank=False, max_length=256)
    subscribe = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.email
        