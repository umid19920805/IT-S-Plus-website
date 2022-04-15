# Generated by Django 4.0.1 on 2022-04-14 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_slide2ensectioncarusel_slide2ensectioninfo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpage_1section',
            name='img2',
            field=models.ImageField(default=1, upload_to='img', verbose_name="Yordamchi suratlar (PNG format va 250x250 o'lchamlar tavsiya etiladi)"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainpage_1section',
            name='img3',
            field=models.ImageField(default=1, upload_to='img', verbose_name="Yordamchi suratlar (PNG format va 232x232 o'lchamlar tavsiya etiladi)"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mainpage_1section',
            name='imgbig',
            field=models.ImageField(upload_to='img', verbose_name="Asosiy surat katta (PNG format va 521x651 o'lchamlar tavsiya etiladi)"),
        ),
    ]