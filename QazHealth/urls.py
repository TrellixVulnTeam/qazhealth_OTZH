from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from QazHealth import views

urlpatterns = [
                  path('', views.index),
                  path('prediction/', views.predict, name='prediction'),
                  path('accounts/', include('allauth.urls')),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
