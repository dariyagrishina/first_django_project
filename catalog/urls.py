from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^tag/(?P<slug>[\w-]+)/$', views.TagView.as_view(), name='tag'),
    # ex: /catalog/5/
# url(r'^(?P<pk>[0-9]+)/$', views.GoodDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^add/(?P<pk>[0-9]+)/$', views.add_item, name='add_item'),
    url(r'^remove/(?P<pk>[0-9]+)/$', views.remove_item, name='remove_item'),
    url(r'^order/$', views.OrderView.as_view(), name='order'),
    url(r'^ordered/$', TemplateView.as_view(template_name='ordered.html'), name='ordered'),
]
