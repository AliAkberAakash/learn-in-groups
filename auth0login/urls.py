from . import views
from django.urls import path, include

import groups

urlpatterns = [
	path('', views.index),
	path('dashboard', views.dashboard),
	path('logout', views.logout),
	path('', include('django.contrib.auth.urls')),
	path('', include('social_django.urls')),
	path('groups', views.groups),
]