from django import forms
from . import models


class Books_all(forms.ModelForm):
    class Meta:
        model = models.Books
        fields = "__all__"