from django.contrib import admin
from django.urls import path, include
from django.views.defaults import page_not_found

handler404 = page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('spanner.urls')),
]
