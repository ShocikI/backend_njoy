"""
URL configuration for NJoy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import re_path, include
from rest_framework import routers
from njoy_backend import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)            # Test URL
router.register(r'events', views.EventViewSet, basename="events")
router.register(r'events/previous', views.PreviousEventViewSet, basename='events/previous')
router.register(r'user_links', views.UserLinkViewSet)   # Test URL
router.register(r'event_links', views.EventLinkViewSet) # Test URL
router.register(r'categories', views.CategoryViewSet)   # Test URL
router.register(r'link_types', views.LinkTypeViewSet)   # Test URL

urlpatterns = [
   re_path(r'^', include(router.urls))
]
