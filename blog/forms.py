from django import forms
from .models import Contact,Email

class ContactFrom(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class EmailFrom(forms.ModelForm):
    class Meta:
        model = Email
        fields = "__all__"