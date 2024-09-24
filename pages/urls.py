from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('history', views.history, name='history'),
    path('vision', views.vision, name='vision'),
    path('goals', views.goals, name='goals'),
    path('organization', views.organization, name='organization'),
    path('work', views.work, name='work'),
    path('team', views.team, name='team'),
    path('mvb', views.mvb, name='mvb'),
    path('pdpolicy', views.pdpolicy, name='pdpolicy'),
    path('pcpolicy', views.pcpolicy, name='pcpolicy'),
    path('ftpolicy', views.ftpolicy, name='ftpolicy'),
    path('esgpolicy', views.esgpolicy, name='esgpolicy'),
    path('ohspolicy', views.ohspolicy, name='ohspolicy'),
    path('amlpolicy', views.amlpolicy, name='amlpolicy'),
    path('abcpolicy', views.abcpolicy, name='abcpolicy'),
    path('joinus', views.joinus, name='joinus'),
    path('contactus', views.contactus, name='contactus'),
    path('sitemap', views.sitemap, name='sitemap'),
    path('disclaimer', views.disclaimer, name='disclaimer'),
    path('awarrange', views.awarrange, name='awarrange'),
]
