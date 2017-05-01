from todo1.models import TodoItem
from todo1.serializers import TodoItemSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.reverse import reverse
from rest_framework.decorators import list_route
from rest_framework.response import Response

# Create your views here.
class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class  = TodoItemSerializer

    def perform_create(self, serializer):
        # Save instance to get the primary key and then update the url
        instance = serializer.save()
        instance.url = reverse('todoitem-detail', args=[instance.pk], request=self.request)
        instance.save()

        # Delete all todo items
        def delete(self, request):
            TodoItem.objects.all().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
