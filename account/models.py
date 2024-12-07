from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=150, unique=True, null=True)  # Store username
    password = models.CharField(max_length=128, null=True)  # Store password (not recommended for security reasons)
    ROLE_CHOICES = [
        ('performer', 'Performer'),
        ('judge', 'Judge'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="performer")

    def __str__(self):
        return f"{self.user.username} - {self.role}"
