# Generated by Django 4.1.7 on 2023-05-22 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FAMILY', '0024_pig_lodgeregistration_delete_lodge_registration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pig_lodgeregistration',
            old_name='paramRegistrationId',
            new_name='lodgeRegistrationId',
        ),
        migrations.RemoveField(
            model_name='pig_lodgeregistration',
            name='parameter',
        ),
        migrations.RemoveField(
            model_name='pig_lodgeregistration',
            name='value',
        ),
        migrations.AddField(
            model_name='pig_lodgeregistration',
            name='duration',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='pig_lodgeregistration',
            name='enteryDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pig_lodgeregistration',
            name='enteryReason',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pig_lodgeregistration',
            name='isFinSejour',
            field=models.BooleanField(default=False, max_length=5),
        ),
        migrations.AddField(
            model_name='pig_lodgeregistration',
            name='leavingDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pig_lodgeregistration',
            name='leavingReason',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pig_lodgeregistration',
            name='lodge',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FAMILY.lodge'),
        ),
        migrations.AddField(
            model_name='pig_lodgeregistration',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
