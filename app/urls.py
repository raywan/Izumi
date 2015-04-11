from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^login/$',views.login_view, name='login'),
    url(r'^logout/$',views.logout_view, name='logout'),
    url(r'^register/$',views.register, name='register'),
    url(r'^directory/$',views.directory, name='directory'),
    url(r'^add/$',views.create_post, name='create_post'),
]
