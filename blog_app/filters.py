import django_filters
from django import forms
from blog_app.models import Post

class PostFilter(django_filters.FilterSet):
    created_on = django_filters.DateTimeFilter(widget = forms.DateInput(attrs={'type':'date'}), lookup_expr="date_exact")

    class Meta:
        model = Post
        fields = ['created_on',]

