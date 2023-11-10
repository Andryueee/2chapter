
from django.contrib import admin
from django.urls import path, re_path, include

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    re_path('application/', include('application.urls'), name = 'application'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]


