# Generated by Django 3.1.6 on 2021-02-11 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='f_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='l_name',
        ),
    ]
