from django.urls import path
from my_site.views import *


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
]
