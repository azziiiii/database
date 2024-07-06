"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from keshe import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('pro/login/', views.LoginView.as_view(), name='prologin'),
    path('pro/view/', views.UserView.as_view(), name='proview'),

    path('function1/', views.function1, name='function1'),
    path('function2/', views.function2, name='function2'),
    path('function3/', views.function3, name='function3'),
    path('function4/', views.function4, name='function4'),
    path('function5/', views.function5, name='function5'),
    path('function6/', views.function6, name='function6'),
    path('function7/', views.function7, name='function7'),
    path('function8/', views.function8, name='function8'),
    path('function9/', views.function9, name='function9'),
    path('function10/', views.function10, name='function10'),
    path('function11/', views.function11, name='function11'),
    path('function12/', views.function12, name='function12'),
    path('function13/', views.function13, name='function13'),
    path('function14/', views.function14, name='function14'),
    path('function15/', views.function15, name='function15'),
    path('function16/', views.function16, name='function16'),
    path('function17/', views.function17, name='function17'),
    path('function18/', views.function18, name='function18'),
    path('function19/', views.function19, name='function19'),
    path('function20/', views.function20, name='function20'),
    # path('students/', views.get_students),
    # path('students/query/', views.ask_students),
    # path('students/sno/check/', views.is_exists_sno),
    # path('students/add/', views.add_student),
    # path('students/modify/', views.modify_student),
    # path('students/del/', views.delete_student),
    # path('students/dels/', views.delete_students),
]
