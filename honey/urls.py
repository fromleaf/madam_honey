"""honey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin

from honey_common.views import MainView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include('rest_framework_docs.urls', namespace='drf_docs')),
]

# Add Apps' URLs
urlpatterns += [
    url(r'^main/$', MainView.as_view(), name='main'),
    url(r'accounts/', include('honey_account.urls', namespace='accounts')),
    url(r'app/', include('honey_app.urls', namespace='honey-app')),
    url(r'chat/', include('honey_chat.urls', namespace='honey-chat')),
]

# Add API's URLs
urlpatterns += [
    url(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
    url(
        r'(?P<version>(v1|v2))/accounts/',
        include('honey_account.routers', namespace='account-routers')
    ),
]
