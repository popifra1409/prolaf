# Generated by Django 4.1.7 on 2023-02-28 08:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accountant',
            fields=[
                ('employeeId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('employeeMat', models.CharField(editable=False, max_length=150)),
                ('firstname', models.CharField(blank=True, max_length=150, null=True)),
                ('lastname', models.CharField(blank=True, max_length=150, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('birthplace', models.CharField(blank=True, max_length=150, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Non precised')], default='Non précisé', max_length=20, null=True)),
                ('status', models.CharField(blank=True, choices=[('single', 'Single'), ('married', 'Married'), ('divorce', 'Divorce'), ('widower ', 'Widower'), ('partner', 'Partner')], default='celibat', max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('photo', models.ImageField(blank=True, default='', null=True, upload_to='')),
                ('function', models.CharField(blank=True, max_length=255, null=True)),
                ('hiringdate', models.DateField()),
                ('seniority', models.IntegerField()),
                ('salary', models.FloatField()),
                ('whatsappnumber', models.CharField(blank=True, max_length=20, null=True)),
                ('facebooklink', models.CharField(blank=True, max_length=255, null=True)),
                ('resourcecontact', models.CharField(blank=True, max_length=20, null=True)),
                ('resourcename', models.CharField(blank=True, max_length=255, null=True)),
                ('isChiefOfDepartment', models.BooleanField(default=False, max_length=5)),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('agentId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('firstname', models.CharField(blank=True, max_length=255, null=True)),
                ('lastname', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('company', models.CharField(blank=True, max_length=255, null=True)),
                ('niu', models.CharField(blank=True, max_length=255, null=True)),
                ('observation', models.CharField(blank=True, max_length=255, null=True)),
                ('bankaccount', models.CharField(blank=True, max_length=255, null=True)),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('departmentId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('dept_name', models.CharField(max_length=50)),
                ('dept_description', models.CharField(blank=True, max_length=200, null=True)),
                ('dept_number', models.CharField(blank=True, max_length=255, null=True)),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateTimeField(auto_now=True)),
                ('dept_parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Departement_parent', to='HRM.department')),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('employeeId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('employeeMat', models.CharField(editable=False, max_length=150)),
                ('firstname', models.CharField(blank=True, max_length=150, null=True)),
                ('lastname', models.CharField(blank=True, max_length=150, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('birthplace', models.CharField(blank=True, max_length=150, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Non precised')], default='Non précisé', max_length=20, null=True)),
                ('status', models.CharField(blank=True, choices=[('single', 'Single'), ('married', 'Married'), ('divorce', 'Divorce'), ('widower ', 'Widower'), ('partner', 'Partner')], default='celibat', max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('photo', models.ImageField(blank=True, default='', null=True, upload_to='')),
                ('function', models.CharField(blank=True, max_length=255, null=True)),
                ('hiringdate', models.DateField()),
                ('seniority', models.IntegerField()),
                ('salary', models.FloatField()),
                ('whatsappnumber', models.CharField(blank=True, max_length=20, null=True)),
                ('facebooklink', models.CharField(blank=True, max_length=255, null=True)),
                ('resourcecontact', models.CharField(blank=True, max_length=20, null=True)),
                ('resourcename', models.CharField(blank=True, max_length=255, null=True)),
                ('isChiefOfDepartment', models.BooleanField(default=False, max_length=5)),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HRM.department')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('agentId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('firstname', models.CharField(blank=True, max_length=255, null=True)),
                ('lastname', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('company', models.CharField(blank=True, max_length=255, null=True)),
                ('niu', models.CharField(blank=True, max_length=255, null=True)),
                ('observation', models.CharField(blank=True, max_length=255, null=True)),
                ('bankaccount', models.CharField(blank=True, max_length=255, null=True)),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('employeeId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('employeeMat', models.CharField(editable=False, max_length=150)),
                ('firstname', models.CharField(blank=True, max_length=150, null=True)),
                ('lastname', models.CharField(blank=True, max_length=150, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('birthplace', models.CharField(blank=True, max_length=150, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Non precised')], default='Non précisé', max_length=20, null=True)),
                ('status', models.CharField(blank=True, choices=[('single', 'Single'), ('married', 'Married'), ('divorce', 'Divorce'), ('widower ', 'Widower'), ('partner', 'Partner')], default='celibat', max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('photo', models.ImageField(blank=True, default='', null=True, upload_to='')),
                ('function', models.CharField(blank=True, max_length=255, null=True)),
                ('hiringdate', models.DateField()),
                ('seniority', models.IntegerField()),
                ('salary', models.FloatField()),
                ('whatsappnumber', models.CharField(blank=True, max_length=20, null=True)),
                ('facebooklink', models.CharField(blank=True, max_length=255, null=True)),
                ('resourcecontact', models.CharField(blank=True, max_length=20, null=True)),
                ('resourcename', models.CharField(blank=True, max_length=255, null=True)),
                ('isChiefOfDepartment', models.BooleanField(default=False, max_length=5)),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HRM.department')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='worker', to='HRM.supervisor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('employeeId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('employeeMat', models.CharField(editable=False, max_length=150)),
                ('firstname', models.CharField(blank=True, max_length=150, null=True)),
                ('lastname', models.CharField(blank=True, max_length=150, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('birthplace', models.CharField(blank=True, max_length=150, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Non precised')], default='Non précisé', max_length=20, null=True)),
                ('status', models.CharField(blank=True, choices=[('single', 'Single'), ('married', 'Married'), ('divorce', 'Divorce'), ('widower ', 'Widower'), ('partner', 'Partner')], default='celibat', max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('photo', models.ImageField(blank=True, default='', null=True, upload_to='')),
                ('function', models.CharField(blank=True, max_length=255, null=True)),
                ('hiringdate', models.DateField()),
                ('seniority', models.IntegerField()),
                ('salary', models.FloatField()),
                ('whatsappnumber', models.CharField(blank=True, max_length=20, null=True)),
                ('facebooklink', models.CharField(blank=True, max_length=255, null=True)),
                ('resourcecontact', models.CharField(blank=True, max_length=20, null=True)),
                ('resourcename', models.CharField(blank=True, max_length=255, null=True)),
                ('isChiefOfDepartment', models.BooleanField(default=False, max_length=5)),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HRM.department')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manager', to='HRM.supervisor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Internal',
            fields=[
                ('contractId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('contract_no', models.CharField(blank=True, max_length=255, null=True)),
                ('dateofcreation', models.DateField(blank=True, max_length=255, null=True)),
                ('duration', models.DateField(blank=True, max_length=255, null=True)),
                ('formofcontract', models.CharField(blank=True, max_length=255, null=True)),
                ('contractupload', models.FileField(blank=True, null=True, upload_to='')),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateTimeField(auto_now=True)),
                ('accountant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HRM.accountant')),
                ('manager', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HRM.manager')),
                ('supervisor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HRM.supervisor')),
                ('worker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HRM.worker')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='External',
            fields=[
                ('contractId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('contract_no', models.CharField(blank=True, max_length=255, null=True)),
                ('dateofcreation', models.DateField(blank=True, max_length=255, null=True)),
                ('duration', models.DateField(blank=True, max_length=255, null=True)),
                ('formofcontract', models.CharField(blank=True, max_length=255, null=True)),
                ('contractupload', models.FileField(blank=True, null=True, upload_to='')),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateTimeField(auto_now=True)),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HRM.client')),
                ('supplier', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HRM.supplier')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('documentId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('numCni', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('cniupload', models.FileField(upload_to='')),
                ('diploma', models.CharField(blank=True, max_length=255, null=True)),
                ('diplomaupload', models.FileField(max_length=255, upload_to='')),
                ('mariagecertificate', models.FileField(blank=True, max_length=255, null=True, upload_to='')),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateTimeField(auto_now=True)),
                ('accountant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HRM.accountant')),
                ('manager', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HRM.manager')),
                ('supervisor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HRM.supervisor')),
                ('worker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HRM.worker')),
            ],
        ),
        migrations.AddField(
            model_name='accountant',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HRM.department'),
        ),
        migrations.AddField(
            model_name='accountant',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='accountant', to='HRM.supervisor'),
        ),
    ]
