# Generated by Django 4.2.1 on 2023-06-12 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_profilepic_profileaddress'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProfilePic',
        ),
    ]
