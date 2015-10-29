from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article


class ArticleListView(ListView):
    context_object_name = "articles"
    model = Article
    template_name = "article_list.html"


class ArticleDetailView(DetailView):
    content_object_name = "article"
    model = Article
    template_name = "article_detail.html"
