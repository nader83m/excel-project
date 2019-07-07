from django.urls import path
from . import views

urlpatterns = [
    path('', views.excel_upload, name='excel_upload'),
    path('excel_upload/', views.excel_upload, name=''),
    path('download/', views.download, name='download'),
]