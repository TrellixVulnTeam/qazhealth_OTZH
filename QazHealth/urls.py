from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin

from QazHealth import views

urlpatterns = [
                  path('', views.index),
                  path('admin/', admin.site.urls),
                  path('prediction/', views.predict, name='prediction'),
                  path('register/', views.register, name='register'),
                  path('login/', views.login, name='login'),
                  path('logout/', views.logout, name='logout'),
                  path('/signin', views.page, name='signin')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)
