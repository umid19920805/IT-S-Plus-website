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
        verbose_name_plural = "Kompaniya ma'lumotlari va u haqida"








######_____START________##########---About-US (Biz haqimizda)---######################
class Biz_Haqimizda_background_tagi(models.Model):
  text = models.CharField("Matn", max_length=30)
  desc = models.TextField("Izoh")
  class Meta:
        verbose_name_plural = 'Biz haqimizda background tagi'

######_____END________##########---About-US (Biz haqimizda)---########################
