from os import POSIX_FADV_DONTNEED
from django.urls import path, include
from rest_framework import routers
from tareas import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskView, 'tasks')

urlpatterns = [
    path('api/v1/', include(router.urls))
]
