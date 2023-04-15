
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
    path('cars/<int:car_id>/add_filling/', views.add_filling, name='add_filling'),
    path('cars/<int:car_id>/add_photo/', views.add_photo, name='add_photo'),
    path('cars/<int:car_id>/assoc_accs/<int:accs_id>/', views.assoc_accs, name='assoc_accs'),
    path('accss/', views.AccsList.as_view(), name='accss_index'),
    path('accss/<int:pk>/', views.AccsDetail.as_view(), name='accss_detail'),
    path('accss/create/', views.AccsCreate.as_view(), name='accss_create'),
    path('accss/<int:pk>/update/', views.AccsUpdate.as_view(), name='accss_update'),
    path('accss/<int:pk>/delete/', views.AccsDelete.as_view(), name='accss_delete'),
]