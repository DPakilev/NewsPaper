from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'article_or_news', 'categories', 'heading', 'text']
