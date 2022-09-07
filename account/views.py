from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from account.serializers import SendPasswordResetEmailSerializer, UserChangePasswordSerializer, UserLoginSerializer, \
    UserPasswordResetSerializer, EditUserSerializer, UserProfileSerializer, UserRegistrationSerializer
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from django.core import serializers


# Generate Token Manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.create_user(request)
        token = get_tokens_for_user(user)
        return Response({'token': token, 'msg': 'Registration Successful'}, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):

        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token': token, 'msg': 'Login Success'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors': {'non_field_errors': ['Email or Password is not Valid']}},
                                status=status.HTTP_404_NOT_FOUND)


class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data
        user_data = {
            # "user": request.user,
            "first_name": data['first_name'],
            "last_name": data['last_name'],
            "experience": data['experience'],
            "b_degree": data['b_degree'],
            "b_institute": data['b_institute'],
            "m_degree": data['m_degree'],
            "m_institute": data['m_institute'],
            "phd_degree": data['phd_degree'],
            "phd_institute": data['phd_institute'],
            # "job_openings": data['job_openings'],
            "birth_date": data['birth_date'],
            "sched_test": data['sched_test'],
            "user_fk": data['user_fk']

        }
        serializer = UserProfileSerializer(data=user_data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            # serializer.data, status=status.HTTP_200_OK
            {
                "user": UserProfileSerializer(user).data,

            })


class UserChangePasswordView(generics.UpdateAPIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    serializer_class = UserChangePasswordSerializer
    model = User

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Password Reset link send. Please check your Email'}, status=status.HTTP_200_OK)


class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, uid, token, format=None):
        serializer = UserPasswordResetSerializer(data=request.data, context={'uid': uid, 'token': token})
        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Password Reset Successfully'}, status=status.HTTP_200_OK)


# For HR to view all resources details
class ResourceView(APIView):
    def get(self, request, format=None, **kwargs):
        resources = User.objects.values(
            'id',
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'residence_city',
            'gender',
            'marital_status',
            'DOB',
            'NIC',
            'passport_no',
            'passport_expiry',
            'blood_group',
            'cnic_img',
            'emp_photo',
            'job_title',
            'dnt',
            'joinig_department',
            'leaving_date',
            'hiring_comments',
            'email',
            'current_salary',
        )
        return Response(resources)


class UserEditView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        # if request.data:
        data = request.data
        try:
            userobj = User.objects.filter(pk=pk).update(**data)
            if userobj:
                return Response(
                    # serializer.data, status=status.HTTP_200_OK
                    {'msg': 'User Data Updated Successfully'}, status=status.HTTP_200_OK
                )

        except Exception as e:
            return Response("User not found in Database")
