from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from homepage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('oferta/', views.oferta, name='oferta'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('omnie/', views.omnie, name='omnie'),
    path('faq/', views.FAQ, name='faq'),
    path('kontakt/', views.kontakt, name='kontakt'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)