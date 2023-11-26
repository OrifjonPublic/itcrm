from rest_framework import serializers
from importlib import import_module

from user.serializers import TeacherSerializer
from .models import Vaqt, Room, Subject, Group


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'room']


class VaqtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaqt
        fields = ['id', 'vaqt']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'fee']


class GroupSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    room = RoomSerializer()
    vaqt = VaqtSerializer()
    subject = SubjectSerializer()

    class Meta:
        model = Group
        fields = ['id', 'name', 'payt', 'room', 'vaqt', 'subject', 'teacher']        
