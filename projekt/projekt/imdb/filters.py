from .models import Movie, Actor
import django_filters

class MovieFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Movie
        fields = ['title']

class ActorFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Actor
        fields = ['last_name','first_name']
