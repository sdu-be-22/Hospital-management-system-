from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import candy,post,category

urlpatterns = [
		path('candy/', candy),
		path('blog/<int:pk>/', post, name='post'),
		path('category/<slug:url>', category),
	]
