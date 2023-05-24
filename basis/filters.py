from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput
from .models import Post


class PostFilter(FilterSet):
   class Meta:
       model = Post
       fields = {
           'title': ['icontains'],
       }
