from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="ชื่อ")
    last_name = models.CharField(max_length=100, verbose_name="นามสกุล")
    email = models.EmailField(unique=True, verbose_name="อีเมล")
