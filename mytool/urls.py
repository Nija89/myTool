from django.urls import path
from . import views
app_name = 'mytool'
urlpatterns = [
    path ('', views.firsFunction, name = 'myFIrstFUnction'),

    path('add/', views.add_task, name='add_task'),

    path('success/', views.success, name = 'success'),


    path('fail/', views.fail, name='fail'),
]