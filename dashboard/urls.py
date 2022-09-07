from django.urls import path
from .views import ProjectView, SprintView, ClientView, ResourceProjectView, DeleteResourceProjectView,AddResourceProjectView

urlpatterns = [
    path('projects/', ProjectView.as_view(), name='projects'),
    path('sprints/', SprintView.as_view(), name='sprints'),
    path('clients/', ClientView.as_view(), name='clients'),
    path('res_proj/', ResourceProjectView.as_view(), name='resource_project'),
    path('add_res8proj/', AddResourceProjectView.as_view(), name='add_resource_project'),
    path('delete_res8proj/<int:pk>', DeleteResourceProjectView.as_view(), name='delete_resource_project'),

]