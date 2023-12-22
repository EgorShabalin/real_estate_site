from django.db import models
from django.utils.translation import gettext as _

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
        verbose_name_plural = "Categories"


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
        verbose_name_plural = "Heating types"


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
        verbose_name_plural = "Parking types"


class Property(models.Model):
    title = models.CharField(max_length=250, verbose_name=_("title"))
    price = models.CharField(max_length=10)
    province = models.CharField(
        max_length=50, choices=IL_LIST, default="Antalya", blank=False, null=False
    )
    district = models.CharField(
        max_length=50, choices=ANTALYA_DIST_LIST, blank=True, null=True
    )
    address = models.CharField(max_length=250, blank=True, null=True)
    floor_number = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    total_floors = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    parking = models.ForeignKey(
        Parking, on_delete=models.CASCADE, null=False, default=[1]
    )
    rooms = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    heating = models.ForeignKey(
        Heating, on_delete=models.CASCADE, null=False, default=[1]
    )
    elevator = models.CharField(
        max_length=50, choices=ELEVATOR, default="No", blank=False, null=False
    )
    frontage = models.CharField(max_length=50, choices=FRONTAGE, blank=True, null=True)
    iskan = models.CharField(
        max_length=50,
        choices=ISKAN,
        default="Yes",
        blank=True,
        null=True,
    )
    expertise = models.CharField(
        max_length=50,
        choices=EXPERTISE,
        default="Yes",
        blank=True,
        null=True,
    )
    residence_permit = models.CharField(
        max_length=50,
        choices=RESIDENCE_PERMIT,
        default="Not possible",
        blank=True,
        null=True,
    )
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=False, default=[1]
    )
    type_of_deal = models.CharField(
        max_length=10, choices=DEAL_TYPES, blank=False, null=False, default="SALE"
    )
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            self.title
            + " | "
            + "Created at: "
            + str(self.created_at)
            + " | "
            + "Updated at: "
            + str(self.updated_at)
        )

    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = "Emlak listesi | Property list"


class Photo(models.Model):
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name="photos"
    )
    photo = models.ImageField(upload_to="photos/")
