from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Business
from apps.categories.models import Category
from django.shortcuts import  get_object_or_404
from django.db.models import Avg
from apps.reviews.forms import ReviewForm



def business_list(request):

    businesses = Business.objects.filter(
        status="active"
    ).select_related(
        "category"
    )


    # Search

    query = request.GET.get("q")

    if query:

        businesses = businesses.filter(
            name__icontains=query
        )


    # Category Filter

    category = request.GET.get("category")

    if category:

        businesses = businesses.filter(
            category__slug=category
        )


    # City Filter

    city = request.GET.get("city")

    if city:

        businesses = businesses.filter(
            city__icontains=city
        )


    # Pagination

    paginator = Paginator(
        businesses,
        9
    )


    page_number = request.GET.get("page")


    page_obj = paginator.get_page(
        page_number
    )


    # Data for dropdowns

    categories = Category.objects.all()


    cities = Business.objects.filter(
        status="active"
    ).values_list(
        "city",
        flat=True
    ).distinct()


    context = {

        "businesses": page_obj,

        "page_obj": page_obj,

        "categories": categories,

        "cities": cities,

    }


    return render(
        request,
        "businesses/business_list.html",
        context
    )




def business_detail(request, slug):


    business = get_object_or_404(
        Business,
        slug=slug,
        status="active"
    )


    # Reviews

    reviews = business.reviews.all().order_by(
    "-created_at")


    average_rating = reviews.aggregate(
    Avg("rating"))["rating__avg"] or 0



    # Similar businesses

    similar_businesses = Business.objects.filter(
        category=business.category,
        status="active"
    ).exclude(
        id=business.id
    )[:3]



    # Review submit

    if request.method == "POST":


        if not request.user.is_authenticated:

            return redirect("login")


        form = ReviewForm(request.POST)


        if form.is_valid():


            review = form.save(commit=False)


            review.business = business

            review.user = request.user


            review.save()


            return redirect(
                "business_detail",
                slug=business.slug
            )


    else:

        form = ReviewForm()



    context = {


        "business": business,


        "reviews": reviews,


        "average_rating": average_rating,


        "form": form,


        "similar_businesses": similar_businesses,

    }


    return render(
        request,
        "businesses/business_detail.html",
        context
    )