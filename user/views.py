from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User, Teacher
from .serializers import (  UserCreateSerializer, UserEditSerializer,
                            CustomTokenObtainPairSerializer, 
                            TeacherSerializer )


class TeacherCreateView(APIView):
    def get(self, request):
        t = Teacher.objects.get(user=request.user)
        ser = TeacherSerializer(t)
        return Response(ser.data)

    def post(self, request):
        ser = TeacherSerializer(data=request.data, context={'request': request})
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(
            {
                'message': 'Xatolik yuz berdi',
                'error': ser.errors
            }
        )

    def patch(self, request):
        t = Teacher.objects.get(user=request.user)
        ser = TeacherSerializer(data=request.data, instance=t, context={'request': request})
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(
            {
                'message': 'Xatolik yuz berdi',
                'error': ser.errors
            }
        )

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserRegisterView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]


class UserEditView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserEditSerializer
    lookup_field = 'id' 
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)