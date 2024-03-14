# Generated by Django 5.0.3 on 2024-03-14 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('mobile_number', models.CharField(max_length=15, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
