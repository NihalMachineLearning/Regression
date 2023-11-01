from django.contrib import admin
from django.urls import path,include
from firstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('index/' , views.result,name='result'),
]