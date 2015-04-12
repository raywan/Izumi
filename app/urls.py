from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^login/$',views.login_view, name='login'),
    url(r'^logout/$',views.logout_view, name='logout'),
    url(r'^register/$',views.register, name='register'),
    url(r'^directory/$',views.directory, name='directory'),
    url(r'^sources/(?P<source_id>[0-9]+)/$',views.source_detail, name='source_detail'),
    url(r'^sources/(?P<source_id>[0-9]+)/update/$',views.update_source, name='update_source'),
    url(r'^profile/(?P<username>.+)/$',views.user_profile, name='user_profile'),
    url(r'^add/$',views.create_source, name='create_source'),
]
