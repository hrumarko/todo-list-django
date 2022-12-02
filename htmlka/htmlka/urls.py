from django.contrib import admin
from django.urls import path, include
from temp.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('temp.urls'), name='temp')
]
