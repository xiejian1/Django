"""djangoDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin

from DjangoApp import views, dbtest

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello$', views.hello),
    url(r'^index$',views.IndexView.as_view(),name="index"),
    url(r'^add$',dbtest.add),
    url(r'^find$',dbtest.find),
    url(r'^update$',dbtest.update),
    url(r'^delete$',dbtest.delete),
    url(r'^search-form$', views.search_form),
    url(r'^search$', views.search),
    url(r'^search-post$', views.search_post),
]

