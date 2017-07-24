from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils import timezone

from .models import Post, Job


class PostListView(ListView):

    model = Post
    paginate_by = 7 #so luong phan tu trong page

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['suggests'] =[]
        for name in Job.objects.all():
            context['suggests'].append(name.name.strip())

        return context

    def get_queryset(self):
        result = super(PostListView, self).get_queryset()

        search = self.request.GET.get('search')
        city = self.request.GET.get('city')
        tags = self.request.GET.get('tags')

        if tags:
            result = result.filter(job__name__unaccent__icontains=tags)

        if city in  ['hn', 'sg']:
            # filter with city
            result = result.filter(city=city)

        return result


class PostDetailView(DetailView):


    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
