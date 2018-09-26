from django.conf.urls import url


from DjangoApp import views, dbtest

urlpatterns = [
    url(r'hello$', views.hello),
    url(r'index$',views.IndexView.as_view(),name="index"),
    url(r'add$',dbtest.add),
    url(r'find$',dbtest.find),
    url(r'update$',dbtest.update),
    url(r'delete$',dbtest.delete),
    url(r'search-form$', views.search_form),
    url(r'search$', views.search),
    url(r'search-post$', views.search_post),
]