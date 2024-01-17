from django.contrib import admin
from django.urls import path, include

# Static settings
from django.conf import settings
from django.conf.urls.static import static

from .views import home_page, cabinet_page

urlpatterns = [
    path('admin/', admin.site.urls),

    # Ui
    path('', home_page, name='home_page'),
    path('cabinet/', cabinet_page, name='cabinet_page'),

    # Login, logout, register
    path('accounts/', include('phone_auth.urls')),

    # Job
    path('jobs/', include('job_app.urls')),

    # Profile
    path('profile/', include('profile_app.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)