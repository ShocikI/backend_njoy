from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from njoy_backend.views.UserViewSet import UserViewSet
from njoy_backend.views.EventViewSet import EventViewSet
from njoy_backend.views.UserLinkViewSet import UserLinkViewSet
from njoy_backend.views.EventLinkViewSet import EventLinkViewSet
from njoy_backend.views.CategoryViewSet import CategoryViewSet
from njoy_backend.views.LinkTypeViewSet import LinkTypeViewSet
from njoy_backend.views.UserEventsView import UserEventsView


router = DefaultRouter()
router.register(r'users', UserViewSet, basename="users")
router.register(r'events', EventViewSet, basename="events")
router.register(r'link_types', LinkTypeViewSet, basename="link-types")
router.register(r'categories', CategoryViewSet, basename="categories")

users_router = NestedDefaultRouter(router, r'users', lookup='username')
users_router.register(r'links', UserLinkViewSet, basename="user-links")

events_router = NestedDefaultRouter(router, r'events', lookup='event')
events_router.register(r'links', EventLinkViewSet, basename='event_links')

urlpatterns = [
    re_path(r'^', include(router.urls)),    
    re_path(r'^', include(users_router.urls)),
    re_path(r'^', include(events_router.urls)),
    path('users/<str:username>/events/', UserEventsView.as_view(), name='user-events'),
]
