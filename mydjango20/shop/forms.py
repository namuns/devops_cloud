from django import forms
from shop.models import Shop, Review, Tag


class ShopForm(forms.ModelForm):
    tags = forms.CharField()

    def save(self):
        # 부모의 save를 호출해주어야 합니다.
        saved_post = super().save()

        # 부모가 한 연산 + 부가적인 연산 수행 가능
        tag_list = []
        tags = self.cleaned_data.get("tags", "")
        for word in tags.split(","):
            tag_name = word.strip()
            tag, __ = Tag.objects.get_or_create(name=tag_name)
            tag_list.append(tag)

            saved_post.tag_set.add(*tag_list)
            saved_post.tag_set.clear()  # 간단 구현을 위해 clear 호출

            return saved_post

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
