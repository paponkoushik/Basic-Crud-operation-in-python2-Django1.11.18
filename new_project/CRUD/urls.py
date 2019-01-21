
from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'^$', views.index, name='index'),
   url(r'^log/', views.index, name='index'),
   url(r'^signup/', views.signup, name='signup'),
   url(r'^reset-password/', views.resetPass, name='resetPass'),
   url(r'^login/', views.login, name='login'),
   url(r'^add-book/', views.addBook, name='addBook'),
   url(r'^create-book/', views.createBook, name='createBook'),
   url(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'),
   url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),
   url(r'^update/(?P<id>\d+)/$', views.update, name='update'),

]