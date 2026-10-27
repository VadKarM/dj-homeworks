from django.views.generic import ListView

from articles.models import Article


class ArticlesList(ListView):
    model = Article
    template_name = 'articles/news.html'
    context_object_name = 'object_list'
    ordering = '-published_at'
