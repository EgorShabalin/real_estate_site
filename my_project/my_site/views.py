from django.shortcuts import render, get_object_or_404

from my_site.models import Property, Photo

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model

from .forms import SignupForm, EditUserForm


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


def search_result(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        proprty_title = Property.objects.filter(title__contains=searched)
        property_description = Property.objects.filter(description__contains=searched)
        property_rooms = Property.objects.filter(rooms__contains=searched)
        property_area = Property.objects.filter(area__contains=searched)
        property_address = Property.objects.filter(address__contains=searched)
        property_price = Property.objects.filter(price__contains=searched)
        searched_items = set()
        for i in proprty_title:
            searched_items.add(i)
        for i in property_description:
            searched_items.add(i)
        for i in property_rooms:
            searched_items.add(i)
        for i in property_area:
            searched_items.add(i)
        for i in property_address:
            searched_items.add(i)
        for i in property_price:
            searched_items.add(i)

    return render(
        request,
        "my_site/search_result.html",
        {
            "searched": searched,
            "searched_items": searched_items,
        },
    )


def contacts(request):
    return render(
        request,
        "my_site/contacts.html",
        {},
    )


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("/")

    else:
        form = SignupForm()

    return render(request, "my_site/signup.html", {"form": form})


@login_required
def profile(request, pk):
    User = get_user_model()
    profile = User.objects.get(id=pk)
    properties = Property.objects.all()
    bookmarks = Property.objects.filter(bookmark=profile)

    return render(
        request,
        "my_site/profile.html",
        {
            "profile": profile,
            "properties": properties,
            "bookmarks": bookmarks,
        },
    )


@login_required
def edit_profile(request):
    User = get_user_model()
    current_user = User.objects.get(id=request.user.id)
    if request.user.is_authenticated:
        form = EditUserForm(request.POST or None, instance=current_user)
        if form.is_valid():
            form.save()
            return redirect("/")

        return render(request, "my_site/edit_profile.html", {"form": form})


@login_required
def bookmark(request, pk):
    property = get_object_or_404(Property, id=request.POST.get("property_detail_id"))
    if property.bookmark.filter(id=request.user.id).exists():
        property.bookmark.remove(request.user)
    else:
        property.bookmark.add(request.user)

    return HttpResponseRedirect(reverse("my_site:property_detail_view", args=[str(pk)]))
