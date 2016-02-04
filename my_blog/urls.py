from django.conf.urls import patterns, include, url
import artical
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'artical.views.home',name='home'),
    url(r'^(?P<id>\d+)/$', 'artical.views.detail', name='detail'),
	url(r'^archives/$', 'artical.views.archives', name = 'archives'),
	url(r'^aboutme/$', 'artical.views.about_me', name = 'about_me'),
	url(r'^tag(?P<tag>\w+)/$', 'artical.views.search_tag', name = 'search_tag'),
	url(r'^search/$','artical.views.blog_search', name = 'search'),
	url(r'^feed/$','RSSFeed()', name = "RSS"),
)
