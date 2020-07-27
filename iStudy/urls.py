from django.contrib import admin
from django.urls import path
from payments import views
from students import views as sviews
from groups import views as gviews
from django.conf import settings
from django.shortcuts import redirect
from iStudy.views import get_index



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',get_index),

    path('payment/new/', views.new_payment, name='new_payment'),
    path('payment/all', views.payments_list, name='payments_list'),

    path('student/new/', sviews.new_student, name='new_student'),
    path('student/all', sviews.students_list, name='students_list'),

    path('group/new/', gviews.new_group, name='new_group'),
    path('group/all', gviews.groups_list, name='groups_list'),
]
