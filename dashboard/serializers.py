from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import Project, Sprint, Clients, ResourceProject
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from account.models import User


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ResrouceProjectSerializer(serializers.ModelSerializer):
    project_fk = serializers.StringRelatedField()
    resource_fk = serializers.StringRelatedField()
    class Meta:
        model = ResourceProject
        fields = [
            'project_fk',
            'resource_fk'
        ]

    def get_project_fk(self, project_fk):
        return project_fk.proj_name

    def get_resource_fk(self, resource_fk):
        return resource_fk.first_name


class AddResrouceProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResourceProject
        fields = [
            'project_fk',
            'resource_fk'
        ]


class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = [
            'project',
            'sprint_no',
            'total_sprint',
            'tasks_assigned',
            'completed_tasks',
            'pending_tasks',
            # tool_used
            'QA_failed',
            'story_points_completed',
            'is_active',
        ]


class ClientSerializer(serializers.ModelSerializer):
    # project = Project.proj_name
    # scrum_master = account.User.first_name
    class Meta:
        model = Clients
        fields = [
            'client_name',
            'project',
            'scrum_master',
        ]
