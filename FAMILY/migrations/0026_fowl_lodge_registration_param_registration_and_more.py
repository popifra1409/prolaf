# Generated by Django 4.1.7 on 2023-05-22 14:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('FAMILY', '0025_rename_paramregistrationid_pig_lodgeregistration_lodgeregistrationid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fowl',
            fields=[
                ('memberId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('member_name', models.CharField(max_length=150)),
                ('birthdate', models.DateField(blank=True, max_length=150, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], default='Male', max_length=20, null=True)),
                ('generation', models.IntegerField(default=0, editable=False)),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateTimeField(auto_now=True)),
                ('colour', models.CharField(max_length=150)),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FAMILY.family')),
                ('father', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Father', to='FAMILY.fowl')),
                ('lodge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='FAMILY.lodge')),
                ('mother', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Mother', to='FAMILY.fowl')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Lodge_Registration',
            fields=[
                ('lodgeRegistrationId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('enteryDate', models.DateField(blank=True, null=True)),
                ('enteryReason', models.CharField(max_length=200, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('isFinSejour', models.BooleanField(default=False, max_length=5)),
                ('leavingDate', models.DateField(blank=True, null=True)),
                ('leavingReason', models.CharField(max_length=200, null=True)),
                ('duration', models.IntegerField(editable=False)),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateTimeField(auto_now=True)),
                ('lodge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FAMILY.lodge')),
            ],
        ),
        migrations.CreateModel(
            name='Param_Registration',
            fields=[
                ('paramRegistrationId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('member_type', models.CharField(blank=True, choices=[('pig', 'Pig'), ('fowl', 'Fowl')], default='Pig', max_length=20, null=True)),
                ('value', models.CharField(max_length=20)),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateTimeField(auto_now=True)),
                ('member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='FAMILY.pig')),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FAMILY.parameter')),
            ],
        ),
        migrations.RemoveField(
            model_name='pig_paramregistration',
            name='parameter',
        ),
        migrations.RemoveField(
            model_name='pig_paramregistration',
            name='pig_name',
        ),
        migrations.DeleteModel(
            name='Pig_LodgeRegistration',
        ),
        migrations.DeleteModel(
            name='Pig_ParamRegistration',
        ),
    ]
