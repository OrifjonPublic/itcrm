from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User, Teacher
# from group.serializers import SubjectSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['status'] = user.status
        token['username']=user.username
        token['id'] = user.id

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        # Get the user object based on the provided credentials
        user = User.objects.get(username=attrs['username'])

        # Add custom fields to the response data
        data['status'] = user.status
        data['username'] = user.username

        return data


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'status']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super(UserCreateSerializer, self).create(validated_data)
        user.set_password(password)
        user.save()
        return user 

    def validate(self, username):
        if User.objects.filter(username=username).exists():
            raise ValidationError(
                {
                'status': False,
                'message': 'Bu username royhatdan o\'tgan, boshqa username kiriting!'
                }
            )
        return username   
    

class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'photo', 'gender', 'phone_number']


class TeacherSerializer(serializers.ModelSerializer):
    user = UserEditSerializer(read_only=True)
    # subject = SubjectSerializer()

    class Meta:
        model = Teacher
        fields = ['id', 'user', 'subject']

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user
        subject = validated_data.pop('subject')
        teacher, created = Teacher.objects.get_or_create(user=user, defaults=validated_data)
        teacher.subject.set(subject)
        if not created:
            for key, value in validated_data.items():
                setattr(teacher, key, value)
            teacher.save()

        return teacher
