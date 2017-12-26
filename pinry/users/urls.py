from django.conf.urls import patterns, url
from django.views.generic import RedirectView
from .views import CreateUser

urlpatterns = patterns('',
    url(r'^private/$', 'pinry.users.views.private', name='private'),
    url(r'^register/$', CreateUser.as_view(), name='register'),
    url(r'^find/$','django.contrib.auth.views.login',{'template_name': 'users/find.html'}, name='find'),
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'users/login.html'}, name='login'),
    url(r'^howtouse/$', 'django.contrib.auth.views.login',
        {'template_name': 'users/howtouse.html'}, name='howtouse'),
    url(r'^logout/$', 'pinry.users.views.logout_user', name='logout'),
)
