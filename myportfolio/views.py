from django.shortcuts import render

from .models import Education, PortfolioItem, Post


def home_view(request):
    items = PortfolioItem.objects.all()
    education = Education.objects.all()
    post = Post.objects.all()
    context = {
        'items': items,
        'education': education,
        'post': post,
    }
    return render(request, 'index.html', context)


def portfolio_detail(request):
    portfolio_item = PortfolioItem.objects.all()
    post = Post.objects.all()
    context = {
        'portfolio_item': portfolio_item,
        'posts': post,
    }
    return render(request, 'portfolio_detail.html', context)
