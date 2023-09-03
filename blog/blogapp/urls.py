from django.urls import path

from blogapp import views

urlpatterns=[
    path('',views.index, name='index'),
    path('post/<str:ok>',views.post, name='post'),#url counter view.counter function name



]