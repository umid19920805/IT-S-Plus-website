from multiprocessing import context
from .models import *
from django.shortcuts import render, redirect, HttpResponseRedirect
import requests


def index(request):
    Mainpage=Mainpage_1section.objects.first()
    slidedesc = Slide2ensectioninfo.objects.first()
    slidecarus = Slide2ensectioninfo.objects.all()
    section444 = Sectioninfor4.objects.first()
    sections333 = Zaybal_section.objects.first()
    # section666 = Sectioninfor6.objects.first()

    context = {
        'Mainpage' : Mainpage,
        'Slidedesc' : slidedesc,
        'Slidecarus' : slidecarus,
        'sec_zaybal' : sections333,
        'sec' : section444,
        # 'sec6' : section666,
    }

    return render(request, 'index.html', context)

def index2(request):

    return render(request, 'index-2.html')



######_____START________##########---About-US (Biz haqimizda)---######################
def about(request):
    about1 = Biz_Haqimizda_background_tagi.objects.all()
    about2 = Biz_Haqimizda_background_tagi2.objects.all()
    about3 = Biz_Haqimizda_asosiy_rasmlari.objects.all()
    about4 = Biz_Haqimizda_asosiy_rasm_matnlari.objects.all()
    about5 = Biz_Haqimizda_statiskalar_tagi.objects.all()
    about6 = Biz_Haqimizda_pastdagi_asosiy_rasmlar.objects.all()
    about7 = Biz_Haqimizda_pastdagi_asosiy_rasmlar_matni.objects.all()
    




    context = {
        'usabout' : about1,
        'usabout2' : about2,
        'usabout3' : about3,
        'usabout4' : about4,
        'usabout5' : about5,
        'usabout6' : about6,
        'usabout7' : about7,


    }

    return render(request, 'about.html', context)
######_____END________##########---About-US (Biz haqimizda)---########################




def blogdetails(request):

    return render(request, 'blog-details.html')

def blog(request):

    return render(request, 'blog.html')

def contact(request):

    return render(request, 'contact.html')

def coursedetails(request):

    return render(request, 'course-details.html')

def courses2(request):

    return render(request, 'courses-2.html')

def courses(request):

    return render(request, 'courses.html')

def faq(request):

    return render(request, 'faq.html')

def index3(request):

    return render(request, 'index-3.html')

def instructorprofile(request):

    return render(request, 'instructor-profile.html')

def instructor(request):

    return render(request, 'instructor.html')

def login(request):

    return render(request, 'login.html')

def price(request):

    return render(request, 'price.html')