# Generated by Django 4.1.7 on 2023-04-24 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FAMILY', '0009_remove_param_registration_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='param_registration',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FAMILY.parameter'),
        ),
    ]