from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from custom_user.models import User

from PIL import Image

from config import (
    HEATING_CHOICES,
    PROPERTY_TYPES,
    IL_LIST,
    ANTALYA_DIST_LIST,
    DEAL_TYPES,
    PARKING_TYPE,
    ELEVATOR,
    FRONTAGE,
    ISKAN,
    EXPERTISE,
    RESIDENCE_PERMIT,
)

from .translation import translate


class Category(models.Model):
    name = models.CharField(
        max_length=25,
        choices=PROPERTY_TYPES,
        default="Apartment",
        blank=False,
        null=False,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = _("Categories")


class Heating(models.Model):
    type = models.CharField(
        max_length=25,
        choices=HEATING_CHOICES,
        default="No heating",
        blank=False,
        null=False,
    )

    def __str__(self) -> str:
        return self.type

    class Meta:
        verbose_name_plural = _("Heating types")


class Parking(models.Model):
    type = models.CharField(
        max_length=25,
        choices=PARKING_TYPE,
        default="Parking on the street",
        blank=False,
        null=False,
    )

    def __str__(self) -> str:
        return self.type

    class Meta:
        verbose_name_plural = _("Parking types")


class Property(models.Model):
    title = models.CharField(
        max_length=250,
        verbose_name="title",
    )
    price = models.CharField(
        "price",
        max_length=10,
    )
    province = models.CharField(
        "province",
        max_length=50,
        choices=IL_LIST,
        default="Antalya",
        blank=False,
        null=False,
    )
    district = models.CharField(
        "district",
        max_length=50,
        choices=ANTALYA_DIST_LIST,
        blank=True,
        null=True,
    )
    address = models.CharField(
        "address",
        max_length=250,
        blank=True,
        null=True,
    )
    floor_number = models.DecimalField(
        "floor_number",
        max_digits=2,
        decimal_places=0,
        default=0,
    )
    total_floors = models.DecimalField(
        "total_floors",
        max_digits=2,
        decimal_places=0,
        default=0,
    )
    parking = models.ForeignKey(
        Parking,
        on_delete=models.CASCADE,
        null=False,
        default=[1],
        verbose_name="parking",
    )
    rooms = models.CharField(
        "rooms",
        max_length=200,
    )
    area = models.CharField(
        "area",
        max_length=200,
    )
    heating = models.ForeignKey(
        Heating,
        on_delete=models.CASCADE,
        null=False,
        default=[1],
        verbose_name="heating",
    )
    elevator = models.CharField(
        "elevator",
        max_length=50,
        choices=ELEVATOR,
        default="No",
        blank=False,
        null=False,
    )
    frontage = models.CharField(
        "frontage",
        max_length=50,
        choices=FRONTAGE,
        blank=True,
        null=True,
    )
    iskan = models.CharField(
        max_length=50,
        choices=ISKAN,
        default="Yes",
        blank=True,
        null=True,
    )
    expertise = models.CharField(
        "expertise",
        max_length=50,
        choices=EXPERTISE,
        default="Yes",
        blank=True,
        null=True,
    )
    residence_permit = models.CharField(
        "residence_permit",
        max_length=50,
        choices=RESIDENCE_PERMIT,
        default="Not possible",
        blank=True,
        null=True,
    )
    description = models.TextField(
        "description",
    )
    en_description = models.TextField(
        "description",
        default="",
    )
    tr_description = models.TextField(
        "description",
        default="",
    )
    ru_description = models.TextField(
        "description",
        default="",
    )
    de_description = models.TextField(
        "description",
        default="",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=False,
        default=[1],
        verbose_name="category",
    )
    type_of_deal = models.CharField(
        "type_of_deal",
        max_length=10,
        choices=DEAL_TYPES,
        blank=False,
        null=False,
        default="SALE",
    )
    active = models.BooleanField(
        "active",
        default=True,
    )
    bookmark = models.ManyToManyField(
        User,
        related_name="bookmarks",
        blank=True,
        verbose_name="bookmark",
    )
    created_at = models.DateTimeField(
        "created_at",
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        "updated_at",
        auto_now=True,
    )

    def __str__(self):
        return (
            "ID"
            + " "
            + str(self.id)
            + " | "
            + str(self.title)
            + " | "
            + _("Created at: ")
            + str(self.created_at)[:19]
            + " | "
            + _("Updated at: ")
            + str(self.updated_at)[:19]
        )

    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = _("Property list")


class Photo(models.Model):
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name="photos",
    )
    photo = models.ImageField(upload_to="photos/")


class Blog(models.Model):
    title = models.CharField(
        max_length=255,
    )
    text = models.TextField()
    en_title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    en_text = models.TextField(
        blank=True,
        null=True,
    )
    tr_title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    tr_text = models.TextField(
        blank=True,
        null=True,
    )
    ru_title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    ru_text = models.TextField(
        blank=True,
        null=True,
    )
    de_title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    de_text = models.TextField(
        blank=True,
        null=True,
    )
    active = models.BooleanField(
        default=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self) -> str:
        return (
            self.title
            + " | "
            + _("Created at: ")
            + str(self.created_at)[:19]
            + " | "
            + _("Updated at: ")
            + str(self.updated_at)[:19]
        )


class BlogPhoto(models.Model):
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name="blog_images",
    )
    image = models.ImageField(upload_to="blog_images/")


class Team(models.Model):
    name = models.CharField(
        max_length=255,
    )
    ava = models.ImageField(
        default=None,
        upload_to="teammates",
        blank=True,
        null=True,
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )
    email = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    bio = models.TextField(
        blank=True,
        null=True,
    )
    active = models.BooleanField(
        default=True,
    )

    def __str__(self) -> str:
        return self.name + " | " + str(self.phone) + " | " + str(self.email)
