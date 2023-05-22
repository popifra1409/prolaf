# Generated by Django 4.1.7 on 2023-05-22 10:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('FAMILY', '0023_alter_pig_birthdate_alter_pig_magnification_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pig_LodgeRegistration',
            fields=[
                ('paramRegistrationId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('value', models.CharField(max_length=20)),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateTimeField(auto_now=True)),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FAMILY.parameter')),
                ('pig_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='FAMILY.pig')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Lodge_Registration',
        ),
    ]
