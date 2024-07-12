from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

from .models import Property, Photo

from django.forms.models import inlineformset_factory


class SignupForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "phone", "first_name", "last_name", "password1", "password2")

    email = forms.CharField(
        widget=forms.EmailInput(attrs={"placeholder": "Your Email"})
    )
    phone = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Your Phone"}))
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Your First name"})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Your Last name"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Your Password"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Repeat Password"})
    )


class EditUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "email", "phone", "password1", "password2")

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Your First name"})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Your Last name"})
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={"placeholder": "Your Email"})
    )
    phone = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Your Phone"}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Your Password"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Repeat Password"})
    )


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Your Email"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Your Password"})
    )


class NewPropertyForm(forms.ModelForm):
    class Meta:
        model = Property

        fields = (
            "title",
            "price",
            "province",
            "district",
            "address",
            "floor_number",
            "total_floors",
            "parking",
            "rooms",
            "area",
            "heating",
            "elevator",
            "frontage",
            "iskan",
            "expertise",
            "residence_permit",
            "description",
            "category",
            "type_of_deal",
            "active",
        )

        widgets = {
            "title": forms.TextInput(),
            "price": forms.TextInput(),
            "province": forms.TextInput(),
            "district": forms.Select(),
            "address": forms.TextInput(),
            "floor_number": forms.TextInput(),
            "total_floors": forms.TextInput(),
            "parking": forms.Select(),
            "rooms": forms.TextInput(),
            "area": forms.TextInput(),
            "heating": forms.Select(),
            "elevator": forms.Select(),
            "frontage": forms.Select(),
            "iskan": forms.Select(),
            "expertise": forms.Select(),
            "residence_permit": forms.Select(),
            "description": forms.Textarea(),
            "category": forms.Select(),
            "type_of_deal": forms.Select(),
            "active": forms.CheckboxInput(),
        }


class EditPropertyForm(forms.ModelForm):
    class Meta:
        model = Property

        fields = (
            "title",
            "price",
            "province",
            "district",
            "address",
            "floor_number",
            "total_floors",
            "parking",
            "rooms",
            "area",
            "heating",
            "elevator",
            "frontage",
            "iskan",
            "expertise",
            "residence_permit",
            "description",
            "category",
            "type_of_deal",
            "active",
        )

        widgets = {
            "title": forms.TextInput(),
            "price": forms.TextInput(),
            "province": forms.TextInput(),
            "district": forms.Select(),
            "address": forms.TextInput(),
            "floor_number": forms.TextInput(),
            "total_floors": forms.TextInput(),
            "parking": forms.Select(),
            "rooms": forms.TextInput(),
            "area": forms.TextInput(),
            "heating": forms.Select(),
            "elevator": forms.Select(),
            "frontage": forms.Select(),
            "iskan": forms.Select(),
            "expertise": forms.Select(),
            "residence_permit": forms.Select(),
            "description": forms.Textarea(),
            "category": forms.Select(),
            "type_of_deal": forms.Select(),
            "active": forms.CheckboxInput(),
        }


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ["photo"]


PhotoFormSet = inlineformset_factory(
    Property, Photo, form=PhotoForm, extra=20, can_delete=True
)
