from django import forms
from shop.models import Shop, Comment, Tag


class ShopForm(forms.ModelForm):
    tags = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            tag_qs = self.instance.tag_set.all()
            tags = ", ".join([tag.name for tag in tag_qs])
            self.fields["tags"].initial = tags

    def _save_m2m(self):
        saved_shop = super()._save_m2m()
        tag_list = []
        tags = self.cleaned_data.get("tags", "")
        for word in tags.split(","):
            tag_name = word.strip()
            tag, __ = Tag.objects.get_or_create(name=tag_name)
            tag_list.append(tag)

        self.instance.tag_set.clear()
        self.instance.tag_set.add(*tag_list)

    class Meta:
        model = Shop
        fields = [
            "category",
            "name",
            "telephone",
            "description",

        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["post", "message"]