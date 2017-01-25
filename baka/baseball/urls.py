

from django.conf.urls import url
from django.contrib import admin
#from .views import
from . import views

app_name = 'baseball' #allows tag on urls etc
urlpatterns = [
    #/baseball /
    url(r'^$', views.index, name='index'), #sets up home page for each individual app section
    #/baseball/batter_id/^ reps begin $reps end
    url(r'^(?P<batter_id>\d+)/$', views.detail, name='detail'), #<id of an object in db>[0-9]+ reps integers from 0-9 and beyond
    url(r'^new_batter/$', views.new_batter, name='new_batter'),
    url(r'^new_statline/(?P<batter_id>\d+)/$', views.new_statline, name='new_statline'),
    url(r'^edit_batter/(?P<batter_id>\d+)/$', views.edit_batter, name='edit_batter'),
    url(r'^my_team/$', views.my_team, name='my_team'),

]
#by having name, I can avoid hard coding my urls
# {% csrf_token %} is a security measure in html for djangodetai
#batters url(r'^batters/$', views.batters, name='batters'),
    #
#url(r'^new_statline/(?P<batter_id>[0-9]+)/$', views.new_statline, name='new_statline'),



# url(r'^(?P<batter_id>\d+)/edit_batter/$', views.edit_batter, name='edit_batter'),
#url(r'^edit_statline/(?P<batter_id>\d+)/$', views.edit_statline, name='edit_statline'),

"""

app_name = 'baseball' #allows tag on urls etc
urlpatterns = [
    #/baseball /
    url(r'^$', views.index, name='index'), #sets up home page for each individual app section
    #/baseball/batter_id/^ reps begin $reps end
    url(r'^(?P<batter_id>[0-9]+)/$', views.detail, name='detail'), #<id of an object in db>[0-9]+ reps integers from 0-9 and beyond
    url(r'^new_batter/$', views.new_batter, name='new_batter'),
    url(r'^new_statline/(?P<batter_id>\d+)/$', views.new_statline, name='new_statline'),
    url(r'^(?P<id>\d+)/edit_batter/$', views.edit_statline, name='edit_batter'),

]



urlpatterns = [
    url(r'^$', index, name='index'),
#    url(r'^create/$', new_batter,name='new_batter'),
    url(r'^(?P<id>\d+)/$', detail, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', edit_batter, name='edit_batter'),
#    url(r'^(?P<id>\d+)/delete/$', delete_batter),
]

from django.conf.urls import url
from django.contrib import admin
from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	)

urlpatterns = [
    url(r'^$', post_list, name='list'),
    url(r'^create/$', post_create),
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', post_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', post_delete),
]


"""