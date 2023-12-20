# Generated by Django 2.2.6 on 2019-11-06 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('aemail', models.CharField(max_length=30)),
                ('bcat', models.CharField(max_length=30)),
                ('aadhar', models.CharField(max_length=30)),
                ('college', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Users',
            },
        ),
    ]
