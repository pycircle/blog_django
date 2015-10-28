from django.conf.urls import include, url
from .views import ArticleListView
urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='home'),
]