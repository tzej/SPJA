from django.db import models

class Actor(models.Model):
    image = models.CharField(default="",max_length=300)
    about = models.CharField(default="",max_length=50000)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)

    def __str__(self):
	    return self.first_name + " " + self.last_name

class Movie(models.Model):
    image = models.CharField(max_length=500)
    trailer = models.CharField(max_length=500)
    title = models.CharField(max_length=100)
    length = models.IntegerField(default=0)
    description = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    rating = models.IntegerField()
    description = models.CharField(max_length=500)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.description

class Watchlist(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name
