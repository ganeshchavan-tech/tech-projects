from rest_framework.serializers import ModelSerializer
from .models import Tasks

class TasksSerializer(ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['task', 'status', 'user']