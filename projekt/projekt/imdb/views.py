from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from .models import Movie, Actor, Review, Watchlist, Comment
from .forms import ReviewForm, WatchlistForm, MovieToWatchlistForm, CommentForm
from .filters import MovieFilter,ActorFilter

def home(request):
   return render(
        request,
        'imdb/index.html',
        {
        }
    )

def movies(request):
    movie = Movie.objects.all()
    movie_filter = MovieFilter(request.GET, queryset=movie)
    return render(
        request,
        'imdb/movies.html',
        {
            'movie': movie,
            'filter' : movie_filter,
        }
    )

def actors(request):
    actor = Actor.objects.all()
    actor_filter = ActorFilter(request.GET, queryset=actor)
    return render(
        request,
        'imdb/actors.html',
        {
            'actor' : actor,
            'actor_filter' : actor_filter,
        }
    )

def movie(request, title):
    movie = get_object_or_404(Movie, title=title)
    actors = Actor.objects.filter(movie=movie)
    comments = Comment.objects.all()
    comment_form = CommentForm()
    review_form = ReviewForm()
    if movie.review_set.all():
        sum = 0;
        for review in movie.review_set.all():
            sum += review.rating

        avg = sum/len(movie.review_set.all())
    else:
        avg = "No reviews"

    #movie = Movie.objects.get(title=title)
    return render(
        request,
        'imdb/movie.html',
        {
            'movie' : movie,
            'review_form' : review_form,
            'comment_form' : comment_form,
            'actors' : actors,
            'avg' : avg,
            'comments' : comments,
        }
    )

def addreview(request, title):
    movie = get_object_or_404(Movie, title=title)
    if request.method == 'POST':
        #print(request.POST)
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_description = review_form.cleaned_data['description']
            review_title = review_form.cleaned_data['title']
            review_rating = review_form.cleaned_data['rating']
            review = Review(movie=movie, description=review_description,title=review_title,rating=review_rating)
            review.save()

            return redirect('movie', title=title)


def addcomment(request, title, _id):
    review = get_object_or_404(Review, pk=_id)
    if request.method == 'POST':
        #print(request.POST)
        comment_form = CommentForm(request.POST)
        print(request.POST)
        if comment_form.is_valid():
            comment_username = comment_form.cleaned_data['username']
            comment_description = comment_form.cleaned_data['description']
            comment = Comment(review=review,username=comment_username, description=comment_description)
            comment.save()

            return redirect('movie', title=title)

def actor(request,my_id):
    actr = get_object_or_404(Actor, pk=my_id)
    movies = Movie.objects.filter(actors=actr)
    return render(
        request,
        'imdb/actor.html',
        {
            'actr' : actr,
            'movies' : movies
        }
    )

def watchlists(request):
    watchlists = Watchlist.objects.all()
    watchlist_form = WatchlistForm()
    return render(
        request,
        'imdb/watchlists.html',
        {
            'watchlist_form' : watchlist_form,
            'watchlists' : watchlists
        }
    )

def watchlist(request,_id):
    watchlist = get_object_or_404(Watchlist, pk=_id)
    movie_towatchlist = MovieToWatchlistForm()
    movies = Movie.objects.filter(watchlist=watchlist)
    return render(
        request,
        'imdb/watchlist.html',
        {
            'watchlist' : watchlist,
            'movie_towatchlist' : movie_towatchlist,
            'movies' : movies
        }
    )

def addtowatchlist(request,_id):
    watchlist = Watchlist.objects.filter(pk=_id)
    if request.method == 'POST':
        #print(request.POST)
        watchlists_form = MovieToWatchlistForm(request.POST)
        if watchlists_form.is_valid():
            list_choices = watchlists_form.cleaned_data['my_choice_field']
            for item in watchlist:
                item.movies.set(list_choices)

            return redirect('watchlist',_id=_id)

def addwatchlist(request):
    if request.method == 'POST':
        #print(request.POST)
        watchlists_form = WatchlistForm(request.POST)
        if watchlists_form.is_valid():
            list_name = watchlists_form.cleaned_data['name']
            list_description = watchlists_form.cleaned_data['description']
            watchlist = Watchlist(name=list_name,description=list_description)
            watchlist.save()

            return redirect('watchlists')

def deletewatchlist(request,id):
    Watchlist.objects.filter(id=id).delete()
    return redirect('watchlists')

def search(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'search/user_list.html', {'filter': user_filter})
