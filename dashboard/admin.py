from django.contrib import admin
from .models import Sprint, Project, UserType, Clients, ResourceProject
from django.db import models


# Register your models here.


# Now register the new EmployeeModelAdmin...

class SprintAdmin(admin.ModelAdmin):
    list_display = [
        'project_fk',
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


class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'proj_name',
        'domain',
        'sub_domain',
        'start_date',
        'end_date',
        # tool_used
        'comment',
        'is_active'
    ]


class UserTypeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user'
    ]


class ClientsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'client_name',
        'project_fk',
        'scrum_master_fk',

    ]


class ResourceProjectAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'resource_fk',
        'project_fk'

    ]


admin.site.register(ResourceProject, ResourceProjectAdmin)
admin.site.register(Sprint, SprintAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(UserType, UserTypeAdmin)
admin.site.register(Clients, ClientsAdmin)
