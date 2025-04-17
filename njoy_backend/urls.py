from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from njoy_backend.views.UserViewSet import UserViewSet
from njoy_backend.views.EventViewSet import EventViewSet
from njoy_backend.views.PreviousEventViewSet import PreviousEventViewSet
from njoy_backend.views.UserLinkViewSet import UserLinkViewSet
from njoy_backend.views.EventLinkViewSet import EventLinkViewSet
from njoy_backend.views.CategoryViewSet import CategoryViewSet
from njoy_backend.views.LinkTypeViewSet import LinkTypeViewSet
from njoy_backend.views.UserEventsView import UserEventsView
from njoy_backend.views.EventLinksByIdView import EventLinksByIdView


router = DefaultRouter()
router.register(r'users', UserViewSet, basename="users")
router.register(r'events', EventViewSet, basename="events")
router.register(r'events/previous', PreviousEventViewSet, basename="events/previous")
router.register(r'link_types', LinkTypeViewSet, basename="link-types")
router.register(r'categories', CategoryViewSet, basename="categories")

nestedUserRouter = NestedDefaultRouter(router, r'users', lookup='username')
nestedUserRouter.register(r'links', UserLinkViewSet, basename="user-links")

router.register(r'event_links', EventLinkViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls)),    
    path('events/<int:pk>/event_links/', EventLinksByIdView.as_view(), name='event-links-by-id'),
    path('users/<str:username>/events/', UserEventsView.as_view(), name='user-events'),
]
