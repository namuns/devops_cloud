from django import forms
from shop.models import Shop, Review


class ShopForm(forms.ModelForm):
    tags = forms.CharField()
    class Meta:
        model = Shop
        fields = [
            "category",
            "name",
            "telephone",
            "description",

        ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["author_name", "message"]
