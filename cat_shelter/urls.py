from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('cats/', views.CatListView.as_view(), name="cat_list"),
    path('cat/<int:pk>/', views.CatDetailView.as_view(), name= 'cat_detail'),
    
]   
