from rest_framework import viewsets
from .serializer import TaskSerializer
from .models import Task
from rest_framework.exceptions import ValidationError

from .logging import logger

def update_task(request, pk):
    logger.debug("Received update request for task ID %s", pk)
    # Your existing code for updating the task

    if validation_fails:  # Replace with your actual validation logic
        logger.error("Your custom error message here")  # Log an error message
        raise ValidationError("Your custom error message here")

# Create your views here.
class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
