# Generated by Django 3.2.6 on 2021-09-17 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_card_container', '0014_rename_blurb_detailpage_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detailpagetag',
            name='content_object',
        ),
        migrations.RemoveField(
            model_name='detailpagetag',
            name='tag',
        ),
        migrations.DeleteModel(
            name='Discipline',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.RemoveField(
            model_name='cardcategory',
            name='discipline',
        ),
        migrations.RemoveField(
            model_name='detailpage',
            name='tags',
        ),
        migrations.DeleteModel(
            name='DetailPageTag',
        ),
    ]
