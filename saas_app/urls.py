from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', About.as_view(), name='about_us'),
    # path('', index, name='index'),
    path('about/', About.as_view(), name='about_page'),
    path('our_facilities/', FacilityView.as_view(), name='our_facilities'),
    path('facilities/<slug:facility_slug>/', FacilityDetailView.as_view(), name='facility_detail'),
    path('our_products/', our_products, name='our_products'),
    path('our_product_details/', product_details, name='our_product_details'),
    path('fabrics/', fabrics, name='fabrics'),
    path('news_updates/', NewsUpdates.as_view(), name='news_updates'),
    path('news/<slug:news_slug>/', NewsDetailView.as_view(), name='news_detail'),
    path('contact/', contact_view, name='contact'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)