from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

from .views import restApi
from .forms import FormFactory
from . import application

router = application.get_router()

urlpatterns = patterns(
    '',
    url(r'^js-locale/(?P<packages>\S+?)/?$', 'django.views.i18n.javascript_catalog'),
    url(r'^js-restAPI/?$', restApi.as_view(), {'router': router, 'url_prefix': '/api'}, name='rest-api'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
