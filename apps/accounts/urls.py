from django.urls import path

from . import views


urlpatterns = [

    path(
        "register/",
        views.register_view,
        name="register"
    ),


    path(
        "profile/",
        views.profile_view,
        name="profile"
    ),


    path(
        "dashboard/",
        views.dashboard_view,
        name="dashboard"
    ),
    path(
    "owner-dashboard/",
    views.owner_dashboard,
    name="owner_dashboard"),

    path(
    "owner/business/add/",
    views.add_business,
    name="add_business"),
    path(
    "owner/business/<int:pk>/edit/",
    views.edit_business,
    name="edit_business"),
    path(
    "owner/business/<int:pk>/delete/",
    views.delete_business,
    name="delete_business"),
    path( "login/", views.login_view, name="login" ), 
    path( "logout/", views.logout_view, name="logout" ),

]