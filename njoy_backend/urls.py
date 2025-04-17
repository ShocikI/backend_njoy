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
from django.urls import path, re_path, include
from rest_framework import routers
from njoy_backend.views.UserViewSet import UserViewSet
from njoy_backend.views.EventViewSet import EventViewSet
from njoy_backend.views.PreviousEventViewSet import PreviousEventViewSet
from njoy_backend.views.UserLinkViewSet import UserLinkViewSet
from njoy_backend.views.EventLinkViewSet import EventLinkViewSet
from njoy_backend.views.CategoryViewSet import CategoryViewSet
from njoy_backend.views.LinkTypeViewSet import LinkTypeViewSet
from njoy_backend.views.UserLinksByUsernameView import UserLinkByUsernameView
from njoy_backend.views.UserEventsView import UserEventsView
from njoy_backend.views.EventLinksByIdView import EventLinksByIdView


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename="users")
router.register(r'events', EventViewSet, basename="events")
router.register(r'events/previous', PreviousEventViewSet, basename="events/previous")
router.register(r'user_links', UserLinkViewSet)
router.register(r'event_links', EventLinkViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'link_types', LinkTypeViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls)),
    path('users/<str:username>/user_links/', UserLinkByUsernameView.as_view(), name='user-links-by-username'),
    path('events/<int:id>/event_links/', EventLinksByIdView.as_view(), name='event-links-by-id'),
    path('users/<str:username>/events/', UserEventsView.as_view(), name='user-events'),
]
