from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'), # 注意这里一定要写开始和结束
    url(r'^cities$', views.cities, name="cities"),
    url(r'^district/([0-9]+)$', views.district, name="district"),
    url(r'^files$', views.files, name="files"),
    url(r'^upload$', views.upload, name="upload"),
    url(r'^page/(?P<pIndex>[0-9]*)/$', views.page, name='page'),
    url(r'^my_ueditor$', views.my_ueditor, name="my_ueditor"),
    url(r'^state$', views.state, name="state"),
    url(r'^middleware$', views.middleware, name="middleware"),
    url(r'^password$', views.password, name="password"),
]