from django.conf.urls import url
from django.contrib import admin
from plotmap import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^upload_file/$', views.upload_file, name='upload_file'),
    url(r'^close/(?P<pk>\d+)/$', views.close, name='close'),
    url(r'^your_file/analyze/(?P<pk>\d+)/$', views.analyze, name='analyze'),
    url(r'^your_file/showdata/(?P<pk>\d+)/$', views.showdata, name='showdata'),
    url(r'^your_file/groupby_district/(?P<pk>\d+)/$', views.groupby_district, name='groupby_district'),
    url(r'^your_file/groupby_state/(?P<pk>\d+)/$', views.groupby_state, name='groupby_state'),
    url(r'^your_file/groupby_college/(?P<pk>\d+)/$', views.groupby_college, name='groupby_college'),
    url(r'^your_file/clean_data/(?P<pk>\d+)/$', views.clean_data, name='clean_data'),
    url(r'^your_file/modify_data/(?P<pk>\d+)/$', views.modify_data, name='modify_data'),
    url(r'^ajax/search/(?P<pk>\d+)/$', views.search, name='search'),
    url(r'^ajax/save_changes/(?P<pk>\d+)/$', views.save_changes, name='save_changes'),
    url(r'^ajax/save_edits/(?P<pk>\d+)/$', views.save_edits, name='save_edits'),
    url(r'^ajax/save_edits_at_modify/(?P<pk>\d+)/$', views.save_edits_at_modify, name='save_edits_at_modify'),
    url(r'^your_file/download/(?P<pk>\d+)/$', views.download, name='download'),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
