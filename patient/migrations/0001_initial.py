# Generated by Django 3.0.6 on 2020-05-30 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=100)),
                ('pemail', models.CharField(max_length=100)),
                ('pphone', models.CharField(max_length=100)),
                ('paddress', models.TextField()),
                ('password', models.CharField(max_length=100)),
                ('report', models.CharField(max_length=100)),
                ('reportof', models.CharField(max_length=100)),
                ('doctornm', models.CharField(max_length=100)),
            ],
        ),
    ]
