# Generated by Django 4.1.1 on 2022-12-14 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_home', '0003_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Callback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_lname', models.CharField(max_length=100)),
                ('c_fname', models.CharField(max_length=100)),
                ('c_email', models.EmailField(max_length=100)),
                ('c_phone', models.CharField(max_length=100)),
            ],
        ),
    ]
