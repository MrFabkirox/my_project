from django import forms

from.models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')
        #if not "com" in email:
        if not extension == "com":
            raise forms.ValidationError("Please use a valid .com email address")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        #validation code here
        return full_name
