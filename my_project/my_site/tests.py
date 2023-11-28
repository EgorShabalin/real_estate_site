from django.test import TestCase
from my_site.models import Category, Heating, Property
from PIL import Image


class PropertyTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="Квартира")
        Property.objects.create(
            title="Квартира 3+1 в Кепезе",
            price="3 000 000 TL",
            city="Antalya",
            district="Kepez",
            address="Kutukcu, sok.0000, b.10",
            # img=Image.open("apple_tree.jpg"),
            rooms="3+1",
            area="150sq.m.",
            heating=Heating.objects.get(type="GAS"),
            description="Просторная квартира в Кепезе с отоплением.",
            category=Category.objects.get(name="Квартира"),
            active=True,
        )

    def test_property(self):
        flat = Property.objects.get(title="Квартира 3+1 в Кепезе")
        self.assertEqual(flat.category.name, "Квартира")
        self.assertEqual(flat.price, "3 000 000 TL")
        self.assertEqual(flat.active, True)
        self.assertEqual(flat.city, "Antalya")
        self.assertEqual(flat.district, "Kepez")
        self.assertEqual(flat.address, "Kutukcu, sok.0000, b.10")
        self.assertEqual(flat.rooms, "3+1")
        self.assertEqual(flat.area, "150sq.m.")
        self.assertEqual(flat.heating, "NO")
        self.assertEqual(flat.description, "Просторная квартира в Кепезе с отоплением.")
        # self.assertEqual(flat.img, Image.open("apple_tree.jpg"))
