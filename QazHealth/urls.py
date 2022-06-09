from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from QazHealth import views

urlpatterns = [
                  path('', views.index),
                  path('prediction/', views.predict, name='prediction'),
                  path('register/', views.register, name='register'),
                  path('login/', views.login, name='login'),
                  path('logout/', views.logout, name='logout')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
