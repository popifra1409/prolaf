# Generated by Django 4.1.7 on 2023-05-19 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FAMILY', '0015_lodgeregistration'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LodgeRegistration',
            new_name='Lodge_Registration',
        ),
        migrations.RenameField(
            model_name='lodge_registration',
            old_name='wwight',
            new_name='weight',
        ),
    ]