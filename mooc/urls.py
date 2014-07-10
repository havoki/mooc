from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mooc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'mooc.core.views.home', name='home'),
    url(r'^contato/$', 'mooc.core.views.contact', name='contact'),
    url(r'^admin/', include(admin.site.urls)),
)
