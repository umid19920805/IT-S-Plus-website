# Generated by Django 4.0.1 on 2022-03-09 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinfo',
            name='Company_phone',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='Company_secondPhone',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
