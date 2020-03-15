from django import forms

from .models import NewsletterUser


class NewsletterUserSignUpForm(forms.ModelForm):
    class Meta:
        model = NewsletterUser
        fields = '__all__'

    def clean_data(self):
        email = self.cleaned_data.get('email')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        return email, first_name, last_name
