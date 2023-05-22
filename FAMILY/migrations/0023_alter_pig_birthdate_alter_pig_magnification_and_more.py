# Generated by Django 4.1.7 on 2023-05-22 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FAMILY', '0022_pig_paramregistration_delete_param_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pig',
            name='birthdate',
            field=models.DateField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='pig',
            name='magnification',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='pig',
            name='post_weaning',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='pig',
            name='pre_magnification',
            field=models.DateTimeField(editable=False, null=True),
        ),
    ]
