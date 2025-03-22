from django.db import models
from django.contrib.auth.models import User
import random

class ConfirmationCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='confirmation_code')
    code = models.CharField(max_length=6)

    @staticmethod
    def generate_code():
        return ''.join(random.choices('0123456789', k=6))

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_code()
        super().save(*args, **kwargs)