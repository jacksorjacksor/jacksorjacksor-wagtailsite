# Generated by Django 3.2.6 on 2021-09-17 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_card_container', '0017_alter_detailpagecategory_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='title',
        ),
    ]
