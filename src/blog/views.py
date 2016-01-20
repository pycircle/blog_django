from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article, Category


class ArticleListView(ListView):
    context_object_name = "articles"
    model = Article
    template_name = "article_list.html"


class ArticleDetailView(DetailView):
    content_object_name = "article"
    model = Article
    template_name = "article_detail.html"

class CategoryListView(ListView):
    context_object_name = "category"
    model = Category
    template_name = "category_list.html"