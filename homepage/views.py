from django.shortcuts import render, get_object_or_404
from category.models import Category
from news.models import News


# Create your views here.
def homepage(request):
    news = News.objects.all()
    context = {
        'news': news,
    }
    return render('request', 'index.html', context)


def news_detail(request, id):
    news = get_object_or_404(News, id=id)

    # increase views
    news.views += 1
    news.save()

    related_news = News.objects.filter(
        category=news.category
    ).exclude(id=news.id)[:4]

    trending_news = News.objects.order_by('-views')[:5]

    categories = Category.objects.all()

    context = {
        'news': news,
        'related_news': related_news,
        'trending_news': trending_news,
        'categories': categories,
    }

    return render(request, 'news_detail.html', context)
