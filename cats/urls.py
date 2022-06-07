from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/3.0/topics/http/urls/
app_name = 'cats'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('main/create/', views.CatCreate.as_view(), name='auto_create'),
    path('main/<int:pk>/update/', views.CatUpdate.as_view(), name='auto_update'),
    path('main/<int:pk>/delete/', views.CatDelete.as_view(), name='auto_delete'),
    path('lookup/', views.MakeView.as_view(), name='make_list'),
    path('lookup/create/', views.MakeCreate.as_view(), name='make_create'),
    path('lookup/<int:pk>/update/', views.BreedUpdate.as_view(), name='make_update'),
    path('lookup/<int:pk>/delete/', views.BreedDelete.as_view(), name='make_delete'),
]