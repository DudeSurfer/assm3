from django.conf.urls import patterns, include, url
from SocNet import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MySocialNetwork.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('^users/$', views.ListUsers),
    url('^(?P<username>\w+)/followers/$', views.ListFollowers),
    url('^(?P<username>\w+)/following/$', views.ListFollowing),
)