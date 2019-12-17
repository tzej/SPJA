from django.contrib import admin

from .models import Movie, Actor, Review, Comment, Watchlist

admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Watchlist)
