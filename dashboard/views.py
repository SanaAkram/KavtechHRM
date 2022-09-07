from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate

from account.renderers import UserRenderer
from .renderers import EmpRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password, check_password
from .models import Project, Sprint, Clients, ResourceProject
from rest_framework import generics
from .serializers import ProjectSerializer, SprintSerializer, ClientSerializer, ResrouceProjectSerializer, \
    AddResrouceProjectSerializer
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


class ResourceProjectView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None, **kwargs):
        resource_project = ResourceProject.objects.all()
        res_data = ResrouceProjectSerializer(resource_project, many=True)
        return Response(res_data.data)


class AddResourceProjectView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        test = request.data
        test_data = {
            "project_fk": test['project_fk'],
            "resource_fk": test['resource_fk'],
        }
        if ResourceProject.objects.filter(**test_data).exists():
            raise Exception('already exists')
        else:
            serializer = AddResrouceProjectSerializer(data=test_data)
            serializer.is_valid(raise_exception=True)
            data = serializer.save()
            return Response(
                # serializer.data, status=status.HTTP_200_OK
                {
                    "Resource_Added": AddResrouceProjectSerializer(data).data,

                }
            )


class DeleteResourceProjectView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        if ResourceProject.objects.filter(pk=pk).exists():
            data = request.data
            userobj = ResourceProject.objects.filter(pk=pk).delete(**data)
            if userobj:
                return Response(
                    # serializer.data, status=status.HTTP_200_OK
                    {'msg': 'Project Resource User Data Deleted Successfully'}, status=status.HTTP_200_OK
                )
            else:
                return Response(
                    # serializer.data, status=status.HTTP_200_OK
                    {'msg': 'Project Resource User not Data Deleted '}, status=status.HTTP_400_BAD_REQUEST
                )


        else:
            return Response(
                {
                    'msg': 'Resource User Data Does not Exists !'
                }
            )