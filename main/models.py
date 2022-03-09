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
