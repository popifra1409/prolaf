# Generated by Django 4.1.7 on 2023-04-24 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FAMILY', '0011_rename_registrationid_parameter_parameterid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parameter',
            old_name='ParameterId',
            new_name='parameterId',
        ),
    ]
