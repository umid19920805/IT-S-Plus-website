from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('index2/', index2, name='index2'),
    path('about/', about, name='about'),
    path('blog-details/', blogdetails, name='blogdetails'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('course-details/', coursedetails, name='coursedetails'),
    path('courses-2/', courses2, name='courses2'),
    path('courses/', courses, name='courses'),
    path('faq/', faq, name='faq'),
    path('index-3/', index3, name='index3'),
    path('instructor-profile/', instructorprofile, name='instructorprofile'),
    path('instructor/', instructor, name='instructor'),
    path('login/', login, name='login'),
    path('price/', price, name='price'),

]