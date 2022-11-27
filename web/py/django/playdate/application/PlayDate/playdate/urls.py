# ░█░█░█▀▄░█░░
# ░█░█░█▀▄░█░░
# ░▀▀▀░▀░▀░▀▀▀
# This file dictates the main paths of our project
# Each of these paths connect to a different app of our project.
# It also connects the static and media files
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('groups/', include('groups.urls')),
    path('events/', include('events.urls')),
    path('about/', include('members.urls')),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# if settings.DEBUG :
#     urlpatterns += static(settings.STATIC_URL,document_root =settings.STATIC_ROOT)

# Use static() to add URL mapping to serve static files during development (only)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
