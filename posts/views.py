from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from .forms import PostForm


def post_create(request):
    form = PostForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user

        instance.save()
    # if request.method == 'POST':
    #     title = request.POST.get('title')
    #     content = request.POST.get('content')
    #     BlogPost.objects.create(title=title, content=content)
    context = {
        'form': form
    }
    return render(request, 'post_form.html', context)


def post_list(request):
    queryset = BlogPost.objects.all()
    context = {
        'object_list': queryset,
        'title': 'List'
    }

    return render(request, 'index.html', context)


def post_detail(request, post_id):
    instance = get_object_or_404(BlogPost, id=post_id)

    context = {
        'title': instance.title,
        'instance': instance,
    }

    return render(request, 'post_detail.html', context)
