from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from user.views import UserRegisterView, UserEditView, CustomTokenObtainPairView, TeacherCreateView
from group.views import (
    RoomListView, RoomEditView, VaqtListView, VaqtEditView, SubjectListView, SubjectEditView
)

urlpatterns = [

    # USER 
    path('signup/', UserRegisterView.as_view(), name='signup'),
    path('edit/<int:id>/', UserEditView.as_view(), name='edit'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),

    # teacher
    path('teacher/', TeacherCreateView.as_view(), name='teacher'),

    # Group
        # room
    path('room/', RoomListView.as_view(), name='room'),
    path('room/edit/<int:id>/', RoomEditView.as_view(), name='edit_room'),

        # vaqt
    path('vaqt/', VaqtListView.as_view(), name='vaqt'),
    path('vaqt/edit/<int:id>/', VaqtEditView.as_view(), name='edit_vaqt'),

        # subject
    path('subject/', SubjectListView.as_view(), name='subject'),
    path('subject/edit/<int:id>/', SubjectEditView.as_view(), name='edit_subject'),    

]