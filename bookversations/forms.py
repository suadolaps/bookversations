from django import forms

from .models import NewsletterUser


class NewsletterUserSignUpForm(forms.ModelForm):
    class Meta:
        model = NewsletterUser
        fields = ['first_name', 'last_name', 'email']

        def clean_data(self):
            email = self.cleaned_data.get('email')
            fname = self.cleaned_data.get('first_name')
            lname = self.cleaned_data.get('last_name')

            return email, fname, lname
