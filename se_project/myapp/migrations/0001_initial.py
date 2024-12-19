# Generated by Django 5.1.1 on 2024-12-19 16:55

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100, verbose_name="ชื่อ")),
                ("last_name", models.CharField(max_length=100, verbose_name="นามสกุล")),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="อีเมล"
                    ),
                ),
            ],
        ),
    ]
