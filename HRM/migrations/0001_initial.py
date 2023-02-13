# Generated by Django 4.1.6 on 2023-02-13 10:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
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
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('contractId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('contract_no', models.CharField(blank=True, max_length=255, null=True)),
                ('dateofcreation', models.DateField(blank=True, max_length=255, null=True)),
                ('duration', models.DateField(blank=True, max_length=255, null=True)),
                ('formofcontract', models.CharField(blank=True, max_length=255, null=True)),
                ('contractupload', models.FileField(blank=True, null=True, upload_to='ContractFile/contract.pdf')),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateTimeField(auto_now=True)),
                ('agent', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HRM.agent')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
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
            name='Employee',
            fields=[
                ('employeeId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('employeeMat', models.CharField(editable=False, max_length=150, unique=True)),
                ('firstname', models.CharField(blank=True, max_length=150, null=True)),
                ('lastname', models.CharField(blank=True, max_length=150, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('birthplace', models.CharField(blank=True, max_length=150, null=True)),
                ('gender', models.CharField(blank=True, choices=[('celibat', 'Célibataire'), ('marie', 'Marié(e)'), ('divorce', 'Divorcé(e)'), ('veuf ', 'Veuf(ve)'), ('concubin', 'Concubinage')], default='celibat', max_length=20, null=True)),
                ('status', models.CharField(blank=True, choices=[('male', 'Masculin'), ('female', 'Féminin'), ('other', 'Non précisé')], default='Non précisé', max_length=255, null=True)),
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
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
                ('superieur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supérieur', to='HRM.employee')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Accountant',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='HRM.employee')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('HRM.employee',),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('agent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='HRM.agent')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('HRM.agent',),
        ),
        migrations.CreateModel(
            name='Client_cont',
            fields=[
                ('contract_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='HRM.contract')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('HRM.contract',),
        ),
        migrations.CreateModel(
            name='Employee_cont',
            fields=[
                ('contract_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='HRM.contract')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('HRM.contract',),
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='HRM.employee')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('HRM.employee',),
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='HRM.employee')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('HRM.employee',),
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('agent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='HRM.agent')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('HRM.agent',),
        ),
        migrations.CreateModel(
            name='Supplier_cont',
            fields=[
                ('contract_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='HRM.contract')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('HRM.contract',),
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='HRM.employee')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('HRM.employee',),
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
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HRM.employee')),
            ],
        ),
        migrations.AddField(
            model_name='contract',
            name='employee',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HRM.employee'),
        ),
        migrations.AddField(
            model_name='contract',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype'),
        ),
    ]
