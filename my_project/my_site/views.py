from django.shortcuts import render, get_object_or_404

from my_site.models import Property, Photo


def property_for_sale_list_view(request):
    for_sale = Property.objects.filter(type_of_deal="SALE")

    return render(request, "my_site/for_sale.html", {"for_sale": for_sale})


def property_for_rent_list_view(request):
    for_rent = Property.objects.filter(type_of_deal="RENT")

    return render(request, "my_site/for_rent.html", {"for_rent": for_rent})


def property_detail_view(request, pk):
    property_detail = get_object_or_404(Property, pk=pk)
    images = property_detail.photos.all()

    return render(
        request,
        "my_site/property_detail.html",
        {"property_detail": property_detail, "images": images},
    )


def property_index_page(request):
    for_sale = Property.objects.filter(type_of_deal="SALE")[:3]
    for_rent = Property.objects.filter(type_of_deal="RENT")[:3]
    images = Photo.objects.all()

    return render(
        request,
        "my_site/index.html",
        {
            "for_sale": for_sale,
            "for_rent": for_rent,
            "images": images,
        },
    )


def contacts(request):
    return render(
        request,
        "my_site/contacts.html",
        {},
    )
