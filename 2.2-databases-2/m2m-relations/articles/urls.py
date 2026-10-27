from django.urls import path

from articles.views import ArticlesList

urlpatterns = [
    path('', ArticlesList.as_view(), name='articles'),
]
