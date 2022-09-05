from django.urls import path
from .views import ProjectView, SprintView, ClientView

urlpatterns = [
    path('projects/', ProjectView.as_view(), name='projects'),
    path('sprints/', SprintView.as_view(), name='sprints'),
    path('clients/', ClientView.as_view(), name='clients'),

]