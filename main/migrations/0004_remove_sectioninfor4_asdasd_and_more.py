# Generated by Django 4.0.4 on 2022-04-16 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_sectioninfor4_asdasd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sectioninfor4',
            name='asdasd',
        ),
        migrations.AddField(
            model_name='sectioninfor4',
            name='sarlavha_tagi',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
