from django.contrib.auth.hashers import make_password, check_password
from rest_framework import serializers
from account.models import User, UserProfile
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import authenticate


class UserRegistrationSerializer(serializers.ModelSerializer):
    # We are writing this because we need confirm password field in our Registration Request
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    confirm_password = serializers.CharField(style={'input_type': 'confirm_password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True},
            'confirm_password': {'write_only': True}
        }

    def create_user(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if request.method == 'POST':
            email = request.data['email']
            name = request.data['name']
            password = request.data['password']
            confirm_password = request.data['confirm_password']
            if password == confirm_password:
                enc_password = make_password(password)
                user = User.objects.create_user(
                    name=name,
                    email=email,
                    password=enc_password,

                )
                return user


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ['email', 'password']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'experience', 'b_degree', 'b_institute',
                  'm_degree', 'm_institute', 'phd_degree', 'phd_institute', 'birth_date', 'sched_test', 'user_fk']


class EditUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            # 'email',
            'name',
            'password',
            # 'is_admin',
            # 'user_type',
            'first_name',
            'last_name',
            'father_name',
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
            # 'leaving_date',
            'hiring_comments',
            'email',
            # 'kav_email',
            'current_salary',
            # 'is_active',
            'leaving_reason',
            'starting_salary',
            'emp_agreement_image',
            'offer_letter_img',
            'NDA_letter_img',
            # 'username',
            'password',
            # 'last_modified_date',
            # 'last_login',
            # 'is_virtual',
            'residence_city',
        ]


class UserChangePasswordSerializer(serializers.Serializer):
    model = User

    """
        Serializer for password change endpoint.
        """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class SendPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print('Encoded UID', uid)
            token = PasswordResetTokenGenerator().make_token(user)
            print('Password Reset Token', token)
            link = 'http://localhost:3000/Kavtech/reset/' + uid + '/' + token
            print('Password Reset Link', link)
            # Send EMail
            body = 'Click Following Link to Reset Your Password ' + link
            data = {
                'subject': 'Reset Your Password',
                'body': body,
                'to_email': user.email
            }
            # Util.send_email(data)
            return attrs
        else:
            raise serializers.ValidationError('You are not a Registered User')


class UserPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)

    class Meta:
        fields = ['password']

    def validate(self, attrs):

        try:
            password = attrs.get('password')
            uid = self.context.get('uid')
            token = self.context.get('token')

            id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise serializers.ValidationError('Token is not Valid or Expired')
            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user, token)
            raise serializers.ValidationError('Token is not Valid or Expired')
