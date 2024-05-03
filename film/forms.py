from django import forms

from .models import Film


class ReviewForm(forms.Form):
    text = forms.CharField(
        label="Текст",
        widget=forms.Textarea(attrs={"class": "form-control"})
    )
    rating = forms.IntegerField(
        label="Оценка",
        widget=forms.NumberInput(attrs={"class": "form-control"}),
        max_value=10,
        min_value=1
    )


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "year": forms.NumberInput(attrs={"class": "form-control"}),
            "rating": forms.NumberInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "genres": forms.SelectMultiple(attrs={"class": "form-control"}),
            "actors": forms.SelectMultiple(attrs={"class": "form-control"}),
        }