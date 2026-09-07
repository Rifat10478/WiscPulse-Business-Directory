from django.shortcuts import render, get_object_or_404

from .models import News

def news_list(request):


 news = News.objects.filter(
    status="published"
)

 return render(
    request,
    "news/news_list.html",
    {
        "news": news
    }
)


def news_detail(request, slug):


 news = get_object_or_404(
    News,
    slug=slug,
    status="published"
)

 return render(
    request,
    "news/news_detail.html",
    {
        "news": news
    }
)

