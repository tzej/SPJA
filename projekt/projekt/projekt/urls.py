"""projekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from imdb import forms, views

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.movies, name='movies'),
    path('watchlists/', views.watchlists, name='watchlists'),
    path('actors/', views.actors, name='actors'),
    path('admin/', admin.site.urls),
    path('actors/<int:my_id>', views.actor, name="actor"),
    path('movies/<str:title>', views.movie, name="movie"),
    path('movies/<str:title>/addreview', views.addreview, name="addreview"),
    path('movies/<str:title>/addcomment/<int:_id>', views.addcomment, name="addcomment"),
    path('watchlists/addwatchlist', views.addwatchlist, name='addwatchlist'),
    path('watchlists/deletewatchlist/<int:id>', views.deletewatchlist, name='deletewatchlist'),
    path('watchlists/<int:_id>', views.watchlist, name="watchlist"),
    path('watchlists/<int:_id>/addtowatchlist', views.addtowatchlist, name="addtowatchlist"),
]
