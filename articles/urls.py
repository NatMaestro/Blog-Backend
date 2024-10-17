from django.urls import path
from .views import ArticleListCreateView, ArticleDetailView

urlpatterns = [
    path('articles/', ArticleListCreateView.as_view(), name='article-list-create'),
    path('articles/<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
]
