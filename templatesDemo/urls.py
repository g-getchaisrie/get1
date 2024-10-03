from django.contrib import admin
from django.urls import path
from templatesApp import views

urlpatterns = [
    path('admin/', admin.site.urls),                  # URL สำหรับหน้าแดชบอร์ดของแอดมิน
    path('', views.renderTemplate, name='home'),     # เส้นทางสำหรับ URL ว่าง (หน้าหลัก)
    path('firstTemplate/', views.renderTemplate, name='firstTemplate'),  # URL สำหรับ firstTemplate
    path('empInfo/', views.renderEmployee, name='empInfo'),  # URL สำหรับ empInfo
]
