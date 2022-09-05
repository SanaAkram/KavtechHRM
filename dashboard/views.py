from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .renderers import EmpRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password, check_password
from .models import Project, Sprint, Clients
from rest_framework import generics
from .serializers import ProjectSerializer, SprintSerializer, ClientSerializer
from rest_framework.views import APIView


# Create your views here.
class ProjectView(APIView):
    def get(self, request, format=None, **kwargs):
        project = Project.objects.all()
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)


# error: AssertionError at /Kavtech/dashboard/projects/'ProjectView' should either include a `queryset` attribute, or override the `get_queryset()` method.


class SprintView(APIView):
    def get(self, request, format=None, **kwargs):
        sprint_data = Sprint.objects.all()
        sprint = SprintSerializer(sprint_data, many=True)
        return Response(sprint.data)


class ClientView(APIView):
    def get(self, request, format=None, **kwargs):
        client_data = Clients.objects.all()
        client = ClientSerializer(client_data, many=True)
        return Response(client.data)
