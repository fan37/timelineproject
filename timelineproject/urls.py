"""timelineproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

#from timeline.views import *
from timeline import views

urlpatterns = [
    url(r'^api/timeline/$', views.timeline_view),
    url(r'^api/timeline/create/$', views.message_create_view),
    url(r'^api/timeline/(?P<num>\d+)/$', views.message_view),
    url(r'^api/timeline/(?P<num>\d+)/delete/$', views.message_delete_view),
    url(r'^api/timeline/(?P<num>\d+)/like/$', views.like_view),
    url(r'^api/timeline/find/$', views.find_view),
    url(r'^api/user/(?P<method>create)/$', views.user_view),
    url(r'^api/user/(?P<method>update)/$', views.user_view),
    url(r'^api/user/(?P<method>list)/$', views.user_view),
    url(r'^api/user/name/$', views.user_view),
    url(r'^api/user/checkpassword/$', views.checkpassword_view),
    url(r'^api/user/setpassword/$', views.setpassword_view),
    url(r'^api/profile/(?P<username>\w+)/$', views.profile_view),
    url(r'^api/profile/$', views.profile_view),
    url(r'^api/login/$', views.login_view),
    url(r'^home/(?P<page>\w+).html$', views.serve_html),

    url(r'^admin/', admin.site.urls),
]
