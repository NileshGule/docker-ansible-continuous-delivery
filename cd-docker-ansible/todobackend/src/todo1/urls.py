from django.conf.urls import url, include
from todo1 import views
from rest_framework.routers import DefaultRouter

# Create a route and register our viewsets with it
router = DefaultRouter(trailing_slash=False)
router.register(r'todos', views.TodoItemViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
    url(r'^', include(router.urls)),
]
