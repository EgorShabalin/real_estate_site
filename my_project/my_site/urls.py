from django.urls import path
from my_site.views import *
from django.contrib.auth import views as auth_views
from .forms import LoginForm


app_name = "my_site"

urlpatterns = [
    path("", property_index_page, name="index"),
    path("property/<int:pk>/", property_detail_view, name="property_detail_view"),
    path(
        "property/for_sale/",
        property_for_sale_list_view,
        name="property_for_sale_list_view",
    ),
    path(
        "property/for_rent/",
        property_for_rent_list_view,
        name="property_for_rent_list_view",
    ),
    path("contacts/", contacts, name="contacts"),
    path("search-result/", search_result, name="search_result"),
    path("signup/", signup, name="signup"),
    path(
        "user_login/",
        auth_views.LoginView.as_view(
            template_name="my_site/login.html", authentication_form=LoginForm
        ),
        name="user_login",
    ),
    path("accounts/profile/<int:pk>/", profile, name="profile"),
    path("edit_profile/", edit_profile, name="edit_profile"),
    path("bookmark/<int:pk>", bookmark, name="bookmark"),
]
