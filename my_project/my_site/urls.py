from django.urls import path
from my_site.views import *
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from django.views.i18n import set_language


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
    path("thank_you/", thank_you, name="thank_you"),
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
    path("favorites/<int:pk>", favorites, name="favorites"),
    path("blog/", blog, name="blog"),
    path("team/", team, name="team"),
    path("set-language/", set_language, name="set_language"),
    path("exchange_rates/", exchange_rates, name="exchange_rates"),
    path("dashboard/", dashboard, name="dashboard"),
    path("new_property/", new_property, name="new_property"),
    path("edit_property/<int:pk>/", edit_property, name="edit_property"),
    path("delete_property/<int:pk>/", delete_property, name="delete_property"),
    path("new_blog_post/", new_blog_post, name="new_blog_post"),
    path("edit_blog_post/<int:pk>/", edit_blog_post, name="edit_blog_post"),
    path("delete_blog_post/<int:pk>/", delete_blog_post, name="delete_blog_post"),
    path("new_team_mate/", new_team_mate, name="new_team_mate"),
    path("edit_team_mate/<int:pk>/", edit_team_mate, name="edit_team_mate"),
    path("delete_team_mate/<int:pk>/", delete_team_mate, name="delete_team_mate"),
    path("dashboard/properties/", dash_properties, name="dash_properties"),
    path("dashboard/blog/", dash_blog, name="dash_blog"),
    path("dashboard/team/", dash_team, name="dash_team"),
]
