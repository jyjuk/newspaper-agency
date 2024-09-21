from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from newspaper.models import Redactor, Newspaper


class RedactorCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience",
        )


class NewspaperForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Newspaper
        fields = "__all__"


class NewspapersSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by title"
            }
        )
    )


class RedactorSearchForm(forms.Form):
    username = forms.CharField(
        max_length=256,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by username"
            }
        )
    )


class TopicSearchForm(forms.Form):
    name = forms.CharField(
        max_length=256,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by topic"
            }
        )
    )
