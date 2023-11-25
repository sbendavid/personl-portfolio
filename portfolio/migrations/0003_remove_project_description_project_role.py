# Generated by Django 4.2.6 on 2023-11-25 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
        migrations.AddField(
            model_name='project',
            name='role',
            field=models.CharField(default='Default Role', max_length=100),
        ),
    ]
