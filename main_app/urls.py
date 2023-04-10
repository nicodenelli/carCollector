
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # route for cars index
    path('cars/', views.cars_index, name='index'),
    # cars details (show page)
    path('cars/<int:car_id>/', views.cars_detail, name='detail'),
    path('cars/create', views.CarCreate.as_view(), name='cars_create'),
     # CBV expect the params to be int:pk (primary key) "The convention name"
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
]