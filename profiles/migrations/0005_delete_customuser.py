# Generated by Django 3.2.21 on 2023-10-10 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]