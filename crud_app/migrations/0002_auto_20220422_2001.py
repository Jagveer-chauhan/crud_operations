# Generated by Django 3.1.13 on 2022-04-22 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='contact',
            new_name='Contact',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='firstname',
            new_name='Firstname',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='lastname',
            new_name='Lastname',
        ),
    ]
