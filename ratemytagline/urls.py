from django.urls import path

from . import views
#Alright alright , no bugs here. Move along >>>>
urlpatterns = [
    path('', views.index, name='index'),
	path('taglines/<int:id>/', views.detail, name='detail'),
]