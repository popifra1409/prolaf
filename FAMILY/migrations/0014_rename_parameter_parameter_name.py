# Generated by Django 4.1.7 on 2023-04-24 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FAMILY', '0013_rename_name_param_registration_parameter_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parameter',
            old_name='parameter',
            new_name='name',
        ),
    ]
