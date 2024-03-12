# Generated by Django 5.0.3 on 2024-03-12 17:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other')], default='M', max_length=1)),
                ('blood', models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=5, null=True)),
                ('hire_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('stitle', models.CharField(max_length=10)),
                ('address', models.TextField(blank=True, null=True)),
                ('contact', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('parent', models.CharField(blank=True, max_length=3, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('stitle', models.CharField(max_length=15)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='EmployeeOffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.employee')),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.office')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='hire_office',
            field=models.ForeignKey(default=100, on_delete=django.db.models.deletion.CASCADE, related_name='hire_office', to='hr.office'),
        ),
        migrations.AddField(
            model_name='employee',
            name='present_office',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='present_office', to='hr.office'),
        ),
        migrations.CreateModel(
            name='EmployeeTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.employee')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.title')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='hire_title',
            field=models.ForeignKey(default=1402, on_delete=django.db.models.deletion.CASCADE, related_name='hire_title', to='hr.title'),
        ),
        migrations.AddField(
            model_name='employee',
            name='present_title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='present_title', to='hr.title'),
        ),
    ]
