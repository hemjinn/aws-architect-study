# Generated by Django 4.1.7 on 2023-05-10 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user',
            new_name='name',
        ),
    ]
