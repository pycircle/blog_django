from django.shortcuts import render
from django.views.generic import ListView
from .models import Article

class ArticleListView(ListView):
    template_name = "article_list.html"
    model = Article
    context_object_name = "articles"