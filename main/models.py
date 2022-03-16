# from turtle import title
from distutils.command.upload import upload
from statistics import mode
from django.db import models

class CompanyInfo(models.Model):
    Company_name = models.CharField(max_length=15,blank=True)
    Company_phone = models.CharField(max_length=15,)
    Company_secondPhone = models.CharField(max_length=15,blank=True)
    Logo = models.ImageField("LOGO : 178x117 o'lcham tavsiya etiladi",upload_to="logo")
    info = models.TextField("Konpaniya haqida ma'lumot",)


    def __str__(self):
      return self.Company_name
    class Meta:
        verbose_name_plural = "Konpaniya ma'lumotlari va u haqida"

class Mainpage_1section(models.Model):
    title = models.CharField(max_length=50,blank=True)
    desc = models.TextField("Sarlavha ostidagi text '160 ta letter tavsiya etiladi",)
    title = models.CharField("#1 bilan yozilgan text",max_length=50,blank=True)
    imgbig = models.ImageField("Asosiy surat katta (PNG format va 521x651 o'lchamlar tavsiya etiladi)",upload_to="img")
    imgbig = models.ImageField("Yordamchi suratlar (PNG format va 250x250 o'lchamlar tavsiya etiladi)",upload_to="img")
    imgbig = models.ImageField("Yordamchi suratlar (PNG format va 232x232 o'lchamlar tavsiya etiladi)",upload_to="img")


    def __str__(self):
      return self.title
    class Meta:
        verbose_name_plural = "Bosh sahifa 1-section"

class Slide2ensectioninfo(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)

class Slide2ensectionCarusel(models.Model):
    icon = models.ImageField(upload_to = "img")
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)

