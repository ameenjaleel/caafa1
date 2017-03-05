from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from resto.views import resto_login,resto_register,resto_logout,resto_index,resto_dash


urlpatterns = [
    # Examples:

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^resto_login/',resto_login,name='resto_login'),
    url(r'^resto_register/',resto_register,name='resto_register'),
    url(r'^resto_logout/',resto_logout,name='resto_logout'),
    url(r'^resto_index/',resto_index,name='resto_index'),
    url(r'^resto_dash/',resto_dash,name='resto_dash'),
    url(r'^$', 'caafa.views.index', name='index'),
    ]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
