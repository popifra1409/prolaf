# Generated by Django 4.1.7 on 2023-07-16 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FAMILY', '0032_alter_param_registration_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='param_registration',
            name='member',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]