import os, dotenv

from django.shortcuts import render, get_object_or_404

from my_site.models import Property, Photo, Blog, Team

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model

from django.utils.translation import gettext as _

from .forms import (
    SignupForm,
    EditUserForm,
    NewPropertyForm,
    EditPropertyForm,
    PhotoFormSet,
)

from .translation import translate

from .utils import get_exchange_rates


def property_for_sale_list_view(request):
    for_sale = Property.objects.filter(type_of_deal="SALE", active=True)

    return render(request, "my_site/for_sale.html", {"for_sale": for_sale})


def property_for_rent_list_view(request):
    for_rent = Property.objects.filter(type_of_deal="RENT", active=True)

    return render(request, "my_site/for_rent.html", {"for_rent": for_rent})


def property_detail_view(request, pk):
    property_detail = get_object_or_404(Property, pk=pk, active=True)
    images = property_detail.photos.all()

    return render(
        request,
        "my_site/property_detail.html",
        {"property_detail": property_detail, "images": images},
    )


def property_index_page(request):
    for_sale = Property.objects.filter(type_of_deal="SALE", active=True)[:3]
    for_rent = Property.objects.filter(type_of_deal="RENT", active=True)[:3]
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
    secret = os.environ["W3F_SECRET"]
    return render(
        request,
        "my_site/contacts.html",
        {
            "secret": secret,
        },
    )


def thank_you(request):
    return render(
        request,
        "my_site/thank_you.html",
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
            return redirect("my_site:user_login")

        return render(request, "my_site/edit_profile.html", {"form": form})


@login_required
def bookmark(request, pk):
    property = get_object_or_404(Property, id=request.POST.get("property_detail_id"))
    if property.bookmark.filter(id=request.user.id).exists():
        property.bookmark.remove(request.user)
    else:
        property.bookmark.add(request.user)

    return HttpResponseRedirect(reverse("my_site:property_detail_view", args=[str(pk)]))


@login_required
def favorites(request, pk):
    User = get_user_model()
    profile = User.objects.get(id=pk)
    bookmarks = Property.objects.filter(bookmark=profile)

    return render(
        request,
        "my_site/favorites.html",
        {
            "profile": profile,
            "bookmarks": bookmarks,
        },
    )


def blog(request):
    blog_list = Blog.objects.filter(active=True)
    for blog in blog_list:
        if not blog.en_title:
            blog.en_title = translate(blog.title, "en")
            blog.save()
        if not blog.en_text:
            blog.en_text = translate(blog.text, "en")
            blog.save()
        if not blog.tr_title:
            blog.tr_title = translate(blog.title, "tr")
            blog.save()
        if not blog.tr_text:
            blog.tr_text = translate(blog.text, "tr")
            blog.save()
        if not blog.ru_title:
            blog.ru_title = translate(blog.title, "ru")
            blog.save()
        if not blog.ru_text:
            blog.ru_text = translate(blog.text, "ru")
            blog.save()
        if not blog.de_title:
            blog.de_title = translate(blog.title, "de")
            blog.save()
        if not blog.de_text:
            blog.de_text = translate(blog.text, "de")
            blog.save()

    return render(request, "my_site/blog.html", {"blog_list": blog_list})


def team(request):
    team = Team.objects.filter(active=True)

    return render(request, "my_site/team.html", {"team": team})


def exchange_rates(request):
    try:
        rates = get_exchange_rates()
        usd_buy = ""
        usd_sell = ""
        eur_buy = ""
        eur_sell = ""
        for k, v in rates.items():
            if k == "USD":
                usd_buy = v["forex_buying"]
                usd_sell = v["forex_selling"]
            if k == "EUR":
                eur_buy = v["forex_buying"]
                eur_sell = v["forex_selling"]
            if k == "RUB":
                rub_buy = v["forex_buying"]
                rub_sell = v["forex_selling"]
    except:
        usd_buy = ""
        usd_sell = ""
        eur_buy = ""
        eur_sell = ""
        rub_buy = ""
        rub_sell = ""

    return render(
        request,
        "my_site/exchange_rates.html",
        {
            "usd_buy": usd_buy,
            "usd_sell": usd_sell,
            "eur_buy": eur_buy,
            "eur_sell": eur_sell,
            "rub_buy": rub_buy,
            "rub_sell": rub_sell,
        },
    )


def dashboard(request):
    properties = Property.objects.all()
    blog_posts = Blog.objects.all()
    team_mates = Team.objects.all()

    return render(
        request,
        "my_site/dashboard.html",
        {
            "properties": properties,
            "blog_posts": blog_posts,
            "team_mates": team_mates,
        },
    )


@login_required
def new_property(request):
    if request.user.is_staff:
        if request.method == "POST":
            form = NewPropertyForm(request.POST, request.FILES)
            if form.is_valid():
                property = form.save(commit=False)
                formset = PhotoFormSet(request.POST, request.FILES, instance=property)
                if formset.is_valid():
                    property.save()
                    formset.save()
                    return redirect("my_site:dashboard")
        else:
            form = NewPropertyForm()
            formset = PhotoFormSet(instance=Property())

        return render(
            request, "my_site/new_property.html", {"form": form, "formset": formset}
        )
    else:
        # Handle unauthorized access
        return redirect("my_site:dashboard")


@login_required
def edit_property(request, pk):
    property = get_object_or_404(Property, pk=pk)

    if request.user.is_staff:
        if request.method == "POST":
            form = EditPropertyForm(request.POST, request.FILES, instance=property)
            formset = PhotoFormSet(request.POST, request.FILES, instance=property)

            if form.is_valid() and formset.is_valid():
                form.save()
                formset.save()
                return redirect("my_site:dashboard")
        else:
            form = EditPropertyForm(instance=property)
            formset = PhotoFormSet(instance=property)

        return render(
            request, "my_site/edit_property.html", {"form": form, "formset": formset}
        )


@login_required
def delete_property(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.user.is_staff:
        property.delete()
        return redirect("my_site:dashboard")
    else:
        return redirect("my_site:dashboard")
