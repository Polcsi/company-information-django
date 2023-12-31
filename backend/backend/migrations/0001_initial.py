# Generated by Django 4.2.5 on 2023-09-17 16:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('companyID', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employeeID', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=18, validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(100)])),
                ('job', models.CharField(choices=[('Software Engineer', 'Software Engineer'), ('Data Scientist', 'Data Scientist'), ('Product Manager', 'Product Manager'), ('Business Analyst', 'Business Analyst'), ('Ui/UX Designer', 'Ui/UX Designer'), ('Manager', 'Manager'), ('Software Tester', 'Software Tester')], default='Software Engineer', max_length=50)),
                ('cv', models.CharField(blank=True, max_length=500, null=True)),
                ('companyID', models.ForeignKey(db_column='companyID', on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='backend.company')),
            ],
        ),
    ]
