# Generated by Django 3.2.6 on 2021-09-16 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_card_container', '0013_detailpage_blurb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detailpage',
            old_name='blurb',
            new_name='description',
        ),
    ]
