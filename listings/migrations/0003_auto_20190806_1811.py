# Generated by Django 2.2.4 on 2019-08-06 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20190804_1147'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listing',
            options={'ordering': ['-list_date']},
        ),
    ]