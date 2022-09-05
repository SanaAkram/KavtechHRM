from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import Project, Sprint, Clients
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from account.models import User


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


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
