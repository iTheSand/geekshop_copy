from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static

from django.urls import path

import mainapp.views as mainapp

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('products/', include('mainapp.urls', namespace='products')),
    path('basket/', include('basketapp.urls', namespace='basket')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('contact/', mainapp.contact, name='contact'),
    path('order/', include('ordersapp.urls'), name='order'),
    path('admin/', include('adminapp.urls', namespace='admin')),

    path('', include('social_django.urls', namespace='social'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
