# Generated by Django 4.1.7 on 2023-05-19 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FAMILY', '0017_rename_reason_lodge_registration_enteryreason'),
    ]

    operations = [
        migrations.AddField(
            model_name='lodge_registration',
            name='leavingDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lodge_registration',
            name='leavingReason',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
