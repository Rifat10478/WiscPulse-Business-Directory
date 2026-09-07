from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from django.contrib.auth import login,logout, authenticate
from apps.businesses.models import Business

from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from apps.businesses.forms import BusinessForm
from django.shortcuts import get_object_or_404

def register_view(request):

 if request.method == "POST":

    form = RegisterForm(request.POST)

    if form.is_valid():

        user = form.save()

        login(request, user)

        return redirect("dashboard")

 else:

    form = RegisterForm()

 return render(
    request,
    "accounts/register.html",
    {
        "form": form
    }
)

@login_required
def profile_view(request):

    return render(
        request,
        "accounts/profile.html"
    )



@login_required
def dashboard_view(request):

    return render(
        request,
        "accounts/dashboard.html"
    )


@login_required
def owner_dashboard(request):


    if request.user.profile.user_type != "owner":

        return redirect("dashboard")



    businesses = Business.objects.filter(
        owner=request.user
    )



    context = {

        "businesses": businesses

    }


    return render(
        request,
        "accounts/owner_dashboard.html",
        context
    )

@login_required
def add_business(request):

    if request.user.profile.user_type != "owner":

        return redirect("dashboard")


    if request.method == "POST":

        form = BusinessForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            business = form.save(
                commit=False
            )

            business.owner = request.user

            business.status = "pending"

            business.save()

            return redirect(
                "owner_dashboard"
            )

    else:

        form = BusinessForm()


    return render(
        request,
        "accounts/add_business.html",
        {
            "form": form
        }
    )


@login_required
def edit_business(request, pk):

    if request.user.profile.user_type != "owner":

        return redirect("dashboard")


    business = get_object_or_404(
        Business,
        pk=pk,
        owner=request.user
    )


    if request.method == "POST":

        form = BusinessForm(
            request.POST,
            request.FILES,
            instance=business
        )


        if form.is_valid():

            business = form.save(
                commit=False
            )

            business.status = "pending"

            business.save()


            return redirect(
                "owner_dashboard"
            )


    else:

        form = BusinessForm(
            instance=business
        )


    return render(
        request,
        "accounts/edit_business.html",
        {
            "form": form,
            "business": business
        }
    )


@login_required
def delete_business(request, pk):

    if request.user.profile.user_type != "owner":

        return redirect("dashboard")


    business = get_object_or_404(
        Business,
        pk=pk,
        owner=request.user
    )


    if request.method == "POST":

        business.delete()

        return redirect(
            "owner_dashboard"
        )


    return render(
        request,
        "accounts/delete_business.html",
        {
            "business": business
        }
    )

def login_view(request):

 if request.method == "POST":

    username = request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(
        request,
        username=username,
        password=password
    )

    if user is not None:

        login(
            request,
            user
        )

        return redirect("dashboard")

    else:

        return render(
            request,
            "accounts/login.html",
            {
                "error": "Invalid username or password."
            }
        )

 return render(
    request,
    "accounts/login.html"
)


def logout_view(request):


    logout(request)


    return redirect("login")