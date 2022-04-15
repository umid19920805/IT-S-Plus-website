# from turtle import title
from distutils.command.upload import upload
from statistics import mode

from distutils.command import upload
from operator import mod

from django.db import models

class CompanyInfo(models.Model):
    Company_name = models.CharField(max_length=15,)
    Company_phone = models.CharField(max_length=15,)
    Company_secondPhone = models.CharField(max_length=15,blank=True)
    Logo = models.ImageField("LOGO : 178x117 o'lcham tavsiya etiladi",upload_to="logo",blank=True)
    info = models.TextField("Kompaniya haqida ma'lumot",)


    def __str__(self):
      return self.Company_name
    class Meta:

        verbose_name_plural = "Konpaniya ma'lumotlari va u haqida"

class Mainpage_1section(models.Model):
    title1 = models.CharField("Title",max_length=70,blank=True)
    desc = models.TextField("Sarlavha ostidagi text '160 ta letter tavsiya etiladi",)
    title = models.CharField("#1 bilan yozilgan text",max_length=50,blank=True)
    imgbig = models.ImageField("Asosiy surat katta (PNG format va 521x651 o'lchamlar tavsiya etiladi)",upload_to="img")
    img3 = models.ImageField("Yordamchi suratlar3 (PNG format va 250x250 o'lchamlar tavsiya etiladi)",upload_to="img")
    img2 = models.ImageField("Yordamchi suratlar2 (PNG format va 232x232 o'lchamlar tavsiya etiladi)",upload_to="img")


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

    class Meta:
        verbose_name_plural = "Kompaniya ma'lumotlari va u haqida"








#################################################_____START________##########---About-US (Biz haqimizda)#################################################
class Biz_Haqimizda_background_tagi(models.Model):
  text = models.CharField("Matn", max_length=40)
  izoh = models.TextField("Izoh")
  class Meta:
        verbose_name_plural = '01_Biz haqimizda background tagi'
############################################################################
class Biz_Haqimizda_background_tagi2(models.Model):
  rasm = models.ImageField(upload_to='about2/')
  text = models.CharField("Matn", max_length=40)
  izoh = models.TextField("Izoh")
  class Meta:
        verbose_name_plural = '02_Biz haqimizda background tagi2'
############################################################################
class Biz_Haqimizda_asosiy_rasmlari(models.Model):
  rasm_521x651 = models.ImageField(upload_to='about3/')
  rasm2_250x250 = models.ImageField(upload_to='about3/')
  rasm3_250x250 = models.ImageField(upload_to='about3/')
  rasm4_250x250 = models.ImageField(upload_to='about3/')
  class Meta:
        verbose_name_plural = '03_Biz haqimizda asosiy rasmlari'
############################################################################
class Biz_Haqimizda_asosiy_rasm_matnlari(models.Model):
  sarlavxa = models.CharField("Sarlavxa", max_length=40)
  text = models.CharField("Matn", max_length=40)
  izoh1 = models.TextField("Izoh")
  izoh2 = models.TextField("Izoh")
  class Meta:
        verbose_name_plural = '04_Biz haqimizda asosiy rasm matnlari'
############################################################################
class Biz_Haqimizda_statiskalar_tagi(models.Model):
  sarlavxa = models.CharField("Sarlavxa", max_length=40)
  matn = models.CharField("Matn", max_length=40)
  rasm_84x100 = models.ImageField(upload_to='about5/')
  rasm_matni = models.CharField("Matn", max_length=40)
  rasm_izohi = models.TextField("Izoh")
  class Meta:
        verbose_name_plural = '05_Biz haqimizda statiskalar tagi'
############################################################################
class Biz_Haqimizda_pastdagi_asosiy_rasmlar_matni(models.Model):
  asosiy_matn = models.CharField(max_length=20)
  asosiy_izoh = models.CharField(max_length=30)
  class Meta:
        verbose_name_plural = '06_Biz haqimizda pastdagi asosiy rasmlar matni'
############################################################################
class Biz_Haqimizda_pastdagi_asosiy_rasmlar(models.Model):
  rasm_305x350 = models.ImageField(upload_to='about6/')
  matn = models.CharField(max_length=30)
  izoh = models.TextField(max_length=200)
  telegram_url = models.CharField(max_length=150)
  instagram_url = models.CharField(max_length=150)
  facebook_url = models.CharField(max_length=150)
  youtube_url = models.CharField(max_length=150)
  class Meta:
        verbose_name_plural = '07_Biz haqimizda pastdagi asosiy rasmlar'
############################################################################

  

#################################################_____END________##########---About-US (Biz haqimizda)---#################################################

