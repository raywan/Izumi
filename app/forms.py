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
    latitude = forms.DecimalField(max_digits=8, decimal_places=6, min_value=-90, max_value=90, initial="0.000000")
    longitude = forms.DecimalField(max_digits=9, decimal_places=6, min_value=-180, max_value=180,initial="0.000000")
    source_type = forms.ChoiceField(choices=SOURCE_CHOICES)
    pathogen_pollution = forms.DecimalField(max_digits=4, decimal_places=1, min_value=0, max_value=100, initial=0)
    inorganic_pollution = forms.DecimalField(max_digits=4, decimal_places=1, min_value=0, max_value=100, initial=0)
    organic_pollution = forms.DecimalField(max_digits=4, decimal_places=1, min_value=0, max_value=100, initial=0)
    macroscopic_pollution = forms.DecimalField(max_digits=4, decimal_places=1, min_value=0, max_value=100, initial=0)
    thermal_pollution = forms.DecimalField(max_digits=4, decimal_places=1, min_value=0, max_value=100, initial=0)
    climate_condition = forms.DecimalField(max_digits=4, decimal_places=1, min_value=0, max_value=100, initial=0)
    depletion_risk = forms.DecimalField(max_digits=4, decimal_places=1, min_value=0, max_value=100, initial=0)
    stress = forms.DecimalField(max_digits=4, decimal_places=1, min_value=0, max_value=100, initial=0)

    # def clean(self):
    #     pass

class AddHistoryForm(forms.Form):
    pathogen_pollution = forms.DecimalField(max_digits=4, decimal_places=1, min_value=0, max_value=100, initial=0)
    inorganic_pollution = forms.DecimalField(max_digits=4, decimal_places=1, min_value=0, max_value=100, initial=0)
    organic_pollution = forms.DecimalField(max_digits=4, decimal_places=1, min_value=0, max_value=100, initial=0)
    macroscopic_pollution = forms.DecimalField(max_digits=4, decimal_places=1, min_value=0, max_value=100, initial=0)
    thermal_pollution = forms.DecimalField(max_digits=4, decimal_places=1, min_value=0, max_value=100, initial=0)
    climate_condition = forms.DecimalField(max_digits=4, decimal_places=1, min_value=0, max_value=100, initial=0)
    depletion_risk = forms.DecimalField(max_digits=4, decimal_places=1, min_value=0, max_value=100, initial=0)
    stress = forms.DecimalField(max_digits=4, decimal_places=1, min_value=0, max_value=100, initial=0)

    def clean(self):
        zero_count = 0
        for k, v in self.cleaned_data.items():
            if not v:
                zero_count += 1
        if zero_count == 8:
            raise forms.ValidationError("No changes made")
        return self.cleaned_data
