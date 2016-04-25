from django.db import models
from django.conf import settings

# Create your models here.
class contents(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    summary = models.TextField()
    workexp = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class templates(models.Model):
    image = models.ImageField()