from django import forms
from .models import Review, Movie, Watchlist, Comment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['movie']

class WatchlistForm(forms.ModelForm):
    class Meta:
        model = Watchlist
        fields = ['name','description']

def get_my_choices():
    return [(movie.pk, movie.title) for movie in Movie.objects.all()]

class MovieToWatchlistForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(MovieToWatchlistForm, self).__init__(*args, **kwargs)
        self.fields['my_choice_field'] = forms.MultipleChoiceField(
            choices=get_my_choices())

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['username','description']
