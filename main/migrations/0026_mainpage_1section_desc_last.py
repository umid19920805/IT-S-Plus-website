# Generated by Django 4.0.4 on 2022-04-15 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_alter_mainpage_1section_img2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpage_1section',
            name='desc_last',
            field=models.TextField(default=1, verbose_name="Sarlavha ostidagi text '160 ta letter tavsiya etiladi_davomi"),
            preserve_default=False,
        ),
    ]
