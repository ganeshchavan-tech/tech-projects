from rest_framework.views import APIView
from .models import Tasks
from accounts.models import Accounts
from .serializers import TasksSerializer
from rest_framework.response import Response

class TasksView(APIView):
    """
    View to handle CRUD operations for tasks.

    Supports GET and POST methods.
    """
    def get(self, request):
        """
        Retrieve tasks based on user permissions.

        Args:
            request (HttpRequest): The request object.

        Returns:
            Response: A response containing the serialized tasks data.
        """
        user = request.user
        queryset = Tasks.objects.all()
        if not user.is_admin:
            queryset = queryset.filter(user=user.id)
        serializer = TasksSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """
        Create a new task.

        Args:
            request (HttpRequest): The request object containing task data.

        Returns:
            Response: A response containing the serialized task data if successful, 
            or error messages if the data is invalid.
        """
        if request.method == 'POST':
            data = request.data.copy()
            username = data.get('username')
            if username:
                user = Accounts.objects.get(username=username)
                if username:
                    data['user'] = user.id
            serializer = TasksSerializer(data=data)
            if serializer.is_valid():
                if not user.is_admin:
                    serializer.save(user=user)
                else:
                    serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)