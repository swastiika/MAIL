# Generated by Django 5.0.6 on 2024-07-01 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='read',
            field=models.BooleanField(default=True),
        ),
    ]
