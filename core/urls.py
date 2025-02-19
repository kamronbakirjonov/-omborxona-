from django.contrib import admin
from django.urls import path, include


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('',include('main.urls')),
    path('sotuvlar/', include('stats.urls')),
    path('accounts/', include('users.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
