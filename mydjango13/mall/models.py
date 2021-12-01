from django.db import models

class Shop(models.Model):
    # id=models.BigAutoField(primary_key=true)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)