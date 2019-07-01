from django.urls import path

from storage import views

app_name = 'storage'
urlpatterns = [
    path('convert/', views.storage, name='convert'),
]