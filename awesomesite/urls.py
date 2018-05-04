from django.contrib import admin
from django.urls import include, path

#somethings not right here either
urlpatterns = [
    path('admin/', admin.site.urls),
]