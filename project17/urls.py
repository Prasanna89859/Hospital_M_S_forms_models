"""
URL configuration for project17 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('application_forms/',application_forms,name='application_forms'),
    path('Docotor_file/',Docotor_file,name='Docotor_file'),
    path('patient_forms/',patient_forms,name='patient_forms'),
    path('appoint_ment/',appoint_ment,name='appoint_ment'),
]

admin.site.site_header='Hospital management'
admin.site.site_title='Hospital management'
