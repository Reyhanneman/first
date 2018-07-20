from django.conf.urls import url
#from qa.views import question

#from django.urls import path

#from . import views

#urlpatterns = [
 #   path('', views.test, name='test'),
 #   path('login/', views.test, name='test'),
 #   path('signup/', views.test, name='test'),
 #   path('question/<int:quetion_id>', views.test, name='test'),
  #  path('ask/', views.test, name='test'),
  #  path('popular/', views.test, name='test'),
  #  path('new/', views.test, name='test'),
#]





from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from ask.qa.views import test

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', test, name = 'home'),
    url(r'^login/', test, name = 'login'),
    url(r'^signup/', test, name = 'signup'),
    url(r'^question/(?P<id>\d+)/', test, name = 'question'),
    url(r'^ask/', test, name = 'ask'),
    url(r'^popular/', test, name = 'popular'),
    url(r'^new/', test, name = 'new'),
    url(r'^admin/', include(admin.site.urls)),
)
