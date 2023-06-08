"""
URL configuration for DJANGO_MVVM project.

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
from django.urls import path
from DJANGO_MVVM import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('ajax', views.ajax),
    path('ajax_emp_list', views.ajax_emp_list),
    path('ajax_emp_detail', views.ajax_emp_detail),
    path('ajax_emp_update', views.ajax_emp_update),
    path('ajax_emp_insert', views.ajax_emp_insert),
    path('ajax_emp_delete', views.ajax_emp_delete),
]
