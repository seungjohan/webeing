from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('wbtotheworld/', admin.site.urls),
    # path('', include("mainPage.urls")),
    path('', include("Account.urls")),
    path('',include('shop.urls')),

    path('cart/',include('cart.urls')),
    path('coupon/',include('coupon.urls')),
    path('order/',include('order.urls')),

    #seo-robots.txt
    path('robots.txt/', TemplateView.as_view(template_name="robots.txt", 
        content_type='text/plain')),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)