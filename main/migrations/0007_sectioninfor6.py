# Generated by Django 4.0.4 on 2022-04-17 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_zaybal_section_desccc2_zaybal_section_iconcard2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sectioninfor6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarlavha_asosiy', models.CharField(max_length=100)),
            ],
        ),
    ]