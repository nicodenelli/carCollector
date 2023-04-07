from django.contrib import admin
# Add the include function to the import below - import path, "include"
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # In this case '' represents the root route localHost:8000
    path('', include('main_app.urls')),
]
