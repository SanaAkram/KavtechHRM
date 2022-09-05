from django.contrib.auth.decorators import login_required
from django_filters import ModelChoiceFilter
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from account.renderers import UserRenderer
from rest_framework.permissions import IsAuthenticated
import account
from rest_framework import viewsets
from account.models import UserProfile
from . import models
from .models import Quizzes, Question, Category, UserSubmittedAnswer
from .serializers import QuestionSerializer, UserSubmittedAnswerSerializer, QuizzesSerializer, CategorySerializer


class Quiz(generics.ListAPIView):
    serializer_class = QuizzesSerializer
    queryset = Quizzes.objects.all()


class CategoryView(generics.ListAPIView):
    def get(self, request, format=None, **kwargs):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class QuizQuestion(APIView):
    def get(self, request, format=None, **kwargs):
        difficulty_level = Question.objects.filter(difficulty_level=kwargs['level'], quiz__category=kwargs['id'])
        serializer = QuestionSerializer(difficulty_level, many=True)
        return Response(serializer.data)


class UserSubView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        test = request.test
        test_data = {
            "user_fk": test['user_fk'],
            "score": test['score'],
        }
        serializer = UserSubmittedAnswerSerializer(test=test_data)
        serializer.is_valid(raise_exception=True)
        test = serializer.save()
        return Response(
            # serializer.data, status=status.HTTP_200_OK
            {
                "test": UserSubmittedAnswerSerializer(test).test,

            }
        )
