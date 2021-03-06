from django.conf.urls import url, include, patterns
from django.contrib.auth.decorators import login_required as auth
# from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib import admin
from profiles.views import UserProfile, Home, EditProfile
import settings

urlpatterns = [
	url(r'^$', Home.as_view(), name="home"),
	url(r'^notices/', include('notices.urls')),
	url(r'^accounts/', include('allauth.urls')),
	# url(r'^api/', include('feeds.urls')),
	url(r'^token/', 'rest_framework_jwt.views.obtain_jwt_token'),
	url(r'^tokenverify/', 'rest_framework_jwt.views.verify_jwt_token'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^user/', include('profiles.urls')),
	# url(r'', include('rest_framework.urls', namespace='rest_framework'))

]

if settings.DEBUG:
	# static files (images, css, javascript, etc.)
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
		'document_root': settings.MEDIA_ROOT}))