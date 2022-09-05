from rest_framework import serializers
from .models import Quizzes, Question, UserSubmittedAnswer, Category
from account.models import UserProfile, User


class QuizzesSerializer(serializers.ModelSerializer):
    difficulty_level = serializers.SerializerMethodField()
    questions = serializers.SerializerMethodField()

    class Meta:
        model = Quizzes
        fields = [
            'title'
        ]

    def get_questions(self, instance):
        questions = Question.objects.filter(quiz__id=instance.id).values(
            # 'title',
            # 'opt_1',
            # 'opt_2',
            # 'opt_3',
            # 'opt_4',
            # 'difficulty_level',
            # 'right_opt',
            # 'score',

        )
        return questions

    def get_difficulty_level(self, instance):
        difficulty_level = Question.objects.filter(difficulty_level=instance.id).values(
            'title',
            'opt_1',
            'opt_2',
            'opt_3',
            'opt_4',
            'difficulty_level',
            # 'right_opt',
            # 'score',
        )
        return difficulty_level


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'id',
            'title',
            'difficulty_level',
            'opt_1',
            'opt_2',
            'opt_3',
            'opt_4',
            'right_opt',
            'score',

        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'description'

        ]

class UserSubmittedAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubmittedAnswer
        fields = [
            'user_fk',
            'score'

        ]


class TestScheduleSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print('Encoded UID', uid)
            token = Token.objects.get(user=user)
            print('Test Schedule Token', token)
            link = 'http://localhost:3000/Kavtech/quiz/test/' + uid + '/' + token
            print('Test Schedule Link', link)
            # Send EMail
            body = 'Click Following Link to Take Your Test ' + link
            data = {
                'subject': 'Kavtech Test',
                'body': body,
                'to_email': user.email
            }
            # Util.send_email(data)
            return attrs
        # else:
        #     raise serializers.ValidationError('You are not a Registered User')
