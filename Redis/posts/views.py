from django.http import JsonResponse  
from django.core.cache import cache
from django.views.generic import ListView

from .models import Post


class PostListView(ListView):
    model = Post

    def get(self, request, *args, **kwargs):
        context = cache.get('posts')

        if not context:
            posts = Post.objects.all().values('id', 'text')
            context = {}
            for i in posts:
                context[f'post_{i["id"]}'] = i
            cache.set_many(context)
        return JsonResponse(context)