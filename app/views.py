from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils import timezone

from .models import Post


class PostListView(ListView):

    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()

        return context

    def get_queryset(self):
        result = super(PostListView, self).get_queryset()

        search = self.request.GET.get('search')
        city = self.request.GET.get('city')
        if city in  ['hn', 'sg']:
            # filter with city
            result = result.filter(city=city)

        if search:
            search_list = search.split(',')
            if len(search_list) >= 1:
                # filter with job
                result = result.filter(job__name__unaccent=search_list[0])
            if len(search_list) >= 2:
                # filter more with restaurant
                result = result.filter(restaurant_namme__unaccent=search_list[1])

        return result


class PostDetailView(DetailView):


    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
