# Generated by Django 3.2.4 on 2022-03-09 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_companyinfo_company_phone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biz_Haqimizda_background_tagi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=30, verbose_name='Matn')),
                ('desc', models.TextField(verbose_name='Izoh')),
            ],
            options={
                'verbose_name_plural': 'Biz haqimizda background tagi',
            },
        ),
        migrations.AlterModelOptions(
            name='companyinfo',
            options={'verbose_name_plural': "Kompaniya ma'lumotlari va u haqida"},
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='Company_name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='Logo',
            field=models.ImageField(blank=True, upload_to='logo', verbose_name="LOGO : 178x117 o'lcham tavsiya etiladi"),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='info',
            field=models.TextField(verbose_name="Kompaniya haqida ma'lumot"),
        ),
    ]
