# Generated by Django 3.2.6 on 2021-09-23 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing_list', '0004_delete_mailinglistentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailinglist',
            name='email_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
