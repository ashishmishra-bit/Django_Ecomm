# Generated by Django 3.1.6 on 2021-02-11 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=20)),
                ('zip_code', models.CharField(max_length=6)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
