from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy
from .models import Post


class LatestPostsFeed(Feed):
    title = 'iRead Blog'
    link = reverse_lazy('home')
    description = 'Latest five blogs on iRead'

    def items(self):
        return Post.objects.filter(published=True)[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.seo_overview

    def item_author_name(self, item):
        return item.author.get_full_name()

    def item_pubdate(self, item):
        return item.timestamp

    def item_categories(self, item):
        return [item.categories.name]

