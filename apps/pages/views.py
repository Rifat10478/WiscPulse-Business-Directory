from django.shortcuts import render

from apps.businesses.models import Business
from apps.categories.models import Category


def home(request):

    featured_businesses = Business.objects.filter(
        status="active",
        is_featured=True
    )[:6]

    categories = Category.objects.all()[:8]

    context = {
        "featured_businesses": featured_businesses,
        "categories": categories,
    }

    return render(
        request,
        "pages/home.html",
        context
    )