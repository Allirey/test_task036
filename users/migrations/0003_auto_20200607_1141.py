# Generated by Django 3.0.7 on 2020-06-07 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_last_request'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='last_request',
            new_name='last_visit',
        ),
    ]
