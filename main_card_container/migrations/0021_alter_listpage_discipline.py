# Generated by Django 3.2.6 on 2021-09-20 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_card_container', '0020_listpage_discipline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listpage',
            name='discipline',
            field=models.ForeignKey(blank='True', null='True', on_delete=django.db.models.deletion.SET_NULL, related_name='discipline_of_list_page', to='main_card_container.discipline'),
        ),
    ]
