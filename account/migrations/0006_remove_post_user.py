# Generated by Django 5.0.4 on 2024-05-28 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_post_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]
