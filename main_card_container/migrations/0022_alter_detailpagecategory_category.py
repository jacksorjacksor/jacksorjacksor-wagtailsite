# Generated by Django 3.2.6 on 2021-09-23 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_card_container', '0021_alter_listpage_discipline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailpagecategory',
            name='category',
            field=models.ForeignKey(blank='False', null='False', on_delete=django.db.models.deletion.CASCADE, related_name='category', to='main_card_container.category'),
        ),
    ]
