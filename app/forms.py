from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=100)
    organization = forms.CharField(label='Organization', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label="Password (again)", widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password1 != password2:
            # self.add_error()
            raise forms.ValidationError("Passwords don't match")

        return cleaned_data

class AddSourceForm(forms.Form):
    SOURCE_CHOICES = (
        ('surface', 'Surface'),
        ('ground', 'Ground'),
        ('frozen', 'Frozen'),
        ('other', 'Other'),
    )
    latitude = forms.DecimalField(max_digits=8, decimal_places=6, min_value=-90, max_value=90)
    longitude = forms.DecimalField(max_digits=9, decimal_places=6, min_value=-180, max_value=180)
    source_type = forms.ChoiceField(choices=SOURCE_CHOICES)
    pathogen_pollution = forms.IntegerField(min_value=0, max_value=100)
    inorganic_pollution = forms.IntegerField(min_value=0, max_value=100)
    organic_pollution = forms.IntegerField(min_value=0, max_value=100)
    macroscopic_pollution = forms.IntegerField(min_value=0, max_value=100)
    thermal_pollution = forms.IntegerField(min_value=0, max_value=100)

    # def clean(self):
    #     pass

class AddEventForm(forms.Form):
    pass
