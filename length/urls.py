from django.urls import path

from length import views

app_name = 'length'
urlpatterns = [
    path('convert/', views.convert, name='convert'),
]