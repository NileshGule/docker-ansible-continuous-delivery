from django.conf.urls import url, include
from todo import views
from rest_framework.routers import DefaultRoute

# Create a route and register our viewsets with it
router = DefaultRoute(trailing_slash=False)
route.register(r'todos', view.todoItemViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
    url(r'^', include(router.urls)),
]
