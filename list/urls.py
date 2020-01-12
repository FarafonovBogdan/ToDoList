from django.urls import path
from . import views

urlpatterns = [
    path('',views.task,name = 'list'),
    path('new_task/<str:pk>/',views.new_task,name = 'new_task'),
    path('delete/<str:pk>/',views.delete,name = 'delete')

]
