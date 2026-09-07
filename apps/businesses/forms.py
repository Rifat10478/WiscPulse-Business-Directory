from django import forms

from .models import Business


class BusinessForm(forms.ModelForm):

    class Meta:

        model = Business

        fields = [
            "name",
            "slug",
            "category",
            "description",
            "logo",
            "cover_image",
            "phone",
            "email",
            "website",
            "address",
            "city",
            "state",
            "postal_code",
            "latitude",
            "longitude",
        ]