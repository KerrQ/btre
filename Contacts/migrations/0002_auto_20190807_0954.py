# Generated by Django 2.2.4 on 2019-08-07 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
