from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('sales/', include('sales.urls')),
    path('preferences/', include('preferences.urls')),
    path('auth/', include('authentication.urls')),
    path('cart/', include('cart.urls')),
      path('dashboard/', include('dashboard.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
