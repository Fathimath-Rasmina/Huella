# Generated by Django 4.1 on 2022-10-21 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_userprofile_profile_picture'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserAddressBook',
        ),
    ]
