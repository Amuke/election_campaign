from django.urls import path
from .views import register_user, home_view, register_member, members_view

urlpatterns = [
    # URL pattern for registering a new user
    path('register/', register_user, name='register_user'),

    # URL pattern for the home page
    path('', home_view, name='home'),

    # URL pattern for registering a new member
    path('register_member/', register_member, name='register_member'),

    # URL pattern for viewing all members
    path('members/', members_view, name='members'),
]
