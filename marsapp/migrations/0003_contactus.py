# Generated by Django 3.0.5 on 2020-05-22 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('marsapp', '0002_auto_20200521_0629'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phoneNo', models.CharField(max_length=13)),
                ('emailId', models.CharField(max_length=220)),
                ('message', models.TextField(max_length=10000)),
                ('reason', models.CharField(max_length=400)),
                ('date_Created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
