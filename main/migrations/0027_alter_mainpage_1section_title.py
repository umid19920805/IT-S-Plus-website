# Generated by Django 4.0.4 on 2022-04-15 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_mainpage_1section_desc_last'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpage_1section',
            name='title',
            field=models.CharField(blank=True, max_length=80, verbose_name='#1 bilan yozilgan text'),
        ),
    ]