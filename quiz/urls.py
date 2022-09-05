from django.urls import path
from .views import Quiz, QuizQuestion, UserSubView, CategoryView

app_name = 'quiz'

urlpatterns = [
    path('', Quiz.as_view(), name='quiz'),
    path('category<int:id>/level<int:level>/', QuizQuestion.as_view(), name='questions'),
    path('test/', UserSubView.as_view(), name='test'),
    path('category/', CategoryView.as_view(), name='category'),
]
