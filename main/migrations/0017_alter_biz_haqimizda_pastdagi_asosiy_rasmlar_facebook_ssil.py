# Generated by Django 3.2.4 on 2022-03-12 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_biz_haqimizda_pastdagi_asosiy_rasmlar_facebook_ssil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biz_haqimizda_pastdagi_asosiy_rasmlar',
            name='facebook_ssil',
            field=models.CharField(max_length=150),
        ),
    ]
