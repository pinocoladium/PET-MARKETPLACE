# Generated by Django 4.2.5 on 2023-10-08 18:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("backend", "0004_alter_client_password"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="status_email",
            field=models.CharField(
                choices=[
                    ("confirmed", "Подтвержден"),
                    ("unconfirmed", "Не подтвержден"),
                ],
                default="unconfirmed",
                max_length=11,
                verbose_name="status client email confirmation",
            ),
        ),
    ]
