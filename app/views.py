from django.shortcuts import render
from django.views.generic.list import ListView
from django.utils import timezone
from .models import Post
import operator
from django.db.models import Q
from functools import reduce

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
        if city not in  ['hn', 'sg']:
            city = ''

        if search:
            search_list = search.split(',')
            result = result.filter(
                reduce(operator.and_,
                       (Q(restaurant_namme__icontains=q) for q in search_list)) and
                reduce(operator.and_,
                       (Q(detail_job__icontains=q) for q in search_list))

                       and
                Q(city__icontains=city)
            )
        return result
