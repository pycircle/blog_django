from django.conf.urls import url
from .views import ArticleListView, ArticleDetailView, CategoryListView
urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='article-list'),
    url(r'^article/(?P<slug>[-\w]+)/$', ArticleDetailView.as_view(), name='article-detail'),
    url(r'^/(?P<slug>[-\w]+)/$', ArticleDetailView.as_view(), name='category-list'),
]