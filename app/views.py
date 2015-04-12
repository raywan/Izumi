from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LoginForm, RegistrationForm, AddSourceForm, AddHistoryForm
from .models import IzumiUser
from api.models import Source, History


## TODO: CHANGE EVERYTHING TO CLASS-BASED VIEWS

def index(request):
    context = {
        'isLoggedIn': request.user.is_authenticated(),
        'user': request.user
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

def source_detail(request, source_id):
    source = get_object_or_404(Source, pk=source_id)
    context = {
        'isLoggedIn': request.user.is_authenticated,
        'source': source
    }
    return render(request, "source_detail.html", context);

def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    if request.user.is_authenticated():
        if request.user == user:
            is_owner = True
        else:
            is_owner = False

    context = {
        'isOwner': is_owner,
        'user': user
    }
    return render(request, "user_profile.html", context);

@login_required(login_url="/login")
def create_source(request):
    form = AddSourceForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        new_source = Source(
            author = IzumiUser.objects.get(user = request.user),
            date_created = timezone.now(),
            last_updated = timezone.now(),
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

    context = {
        'isLoggedIn': request.user.is_authenticated,

        'form': form
    }
    return render(request, 'add.html', context)

@login_required(login_url="/login")
def update_source(request, source_id):
    source = get_object_or_404(Source, pk=source_id)
    form = AddHistoryForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        new_history = History(
            source_id = source,
            author = IzumiUser.objects.get(user = request.user),
            date_created = timezone.now(),
            latitude = source.latitude,
            longitude = source.longitude,
            d_pathogen_pollution = form.cleaned_data.get('pathogen_pollution') - source.pathogen_pollution,
            d_inorganic_pollution = form.cleaned_data.get('inorganic_pollution') - source.inorganic_pollution,
            d_organic_pollution = form.cleaned_data.get('organic_pollution') - source.organic_pollution,
            d_macroscopic_pollution = form.cleaned_data.get('macroscopic_pollution') - source.macroscopic_pollution,
            d_thermal_pollution = form.cleaned_data.get('thermal_pollution') - source.thermal_pollution,
            d_climate_condition = form.cleaned_data.get('thermal_pollution') - source.climate_condition,
            d_depletion_risk = form.cleaned_data.get('thermal_pollution') - source.depletion_risk,
            d_stress = form.cleaned_data.get('thermal_pollution') - source.stress,
        )
        new_history.save()
        return HttpResponseRedirect(reverse('source_detail', kwargs={"source_id":source.id}))
    context = {
        'source': source,
        'form': form
    }
    return render(request, "update_source.html", context);
