from django.conf.urls import url, include
from .views import ArticleListView, ArticleDetailView
from django.contrib.flatpages import views

urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='article-list'),
    url(r'^article/(?P<slug>[-\w]+)/$', ArticleDetailView.as_view(), name='article-detail'),
    url(r'^about/(?P<url>.*/)$', views.flatpage, name='about-pages'),
]
