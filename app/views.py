from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LoginForm, RegistrationForm, AddSourceForm
from .models import IzumiUser
from api.models import Source, Event


## TODO: CHANGE EVERYTHING TO CLASS-BASED VIEWS

def index(request):
    context = {
        'isLoggedIn': request.user.is_authenticated()
    }
    return render(request, "index.html", context)

def login_view(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return HttpResponseRedirect('/')
    return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        new_user = User.objects.create_user(
            username=form.cleaned_data.get('username'),
            email=form.cleaned_data.get('email'),
            first_name=form.cleaned_data.get('first_name'),
            last_name=form.cleaned_data.get('last_name'),
            password=form.cleaned_data.get('password1'),
        )
        new_izumi_user = IzumiUser(
            user=new_user,
            organization=form.cleaned_data.get('organization'),
        )
        new_izumi_user.save()
        return HttpResponseRedirect('/')
    return render(request, 'register.html', {'form':form})

def directory(request):
    context = {
        'isLoggedIn': request.user.is_authenticated
    }
    return render(request, "directory.html", context)

@login_required(login_url="/login")
def create_post(request):
    form = AddSourceForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        new_source = Source(
            author = IzumiUser.objects.get(user = request.user),
            date_created = timezone.now(),
            last_update = timezone.now(),
            latitude = form.cleaned_data.get('latitude'),
            longitude = form.cleaned_data.get('longitude'),
            source_type = form.cleaned_data.get('source_type'),
            pathogen_pollution = form.cleaned_data.get('pathogen_pollution'),
            inorganic_pollution = form.cleaned_data.get('inorganic_pollution'),
            organic_pollution = form.cleaned_data.get('organic_pollution'),
            macroscopic_pollution = form.cleaned_data.get('macroscopic_pollution'),
            thermal_pollution = form.cleaned_data.get('thermal_pollution'),
        )
        new_source.save()
        return HttpResponseRedirect('/')

    return render(request, 'add.html', {'form':form})
