# Generated by Django 3.1 on 2020-10-13 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewpost', '0002_reviewmodel_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewmodel',
            name='name',
        ),
    ]