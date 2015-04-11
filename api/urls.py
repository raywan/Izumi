from django.conf.urls import url
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^sources/$',views.SourceList.as_view()),
    url(r'^sources/(?P<pk>[0-9]+)/$',views.SourceDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
