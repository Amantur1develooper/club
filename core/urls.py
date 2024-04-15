from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import *



urlpatterns = [
    path('users/', UserListCreateAPIView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),

    path('documentation/', DocumentationListCreateAPIView.as_view(), name='documentation-list'),
    path('documentation/<int:pk>/', DocumentationRetrieveUpdateDestroyAPIView.as_view(), name='documentation-detail'),

    path('topics-documentation/', TopicsDocumentationListCreateAPIView.as_view(), name='topics-documentation-list'),
    path('topics-documentation/<int:pk>/', TopicsDocumentationRetrieveUpdateDestroyAPIView.as_view(),
         name='topics-documentation-detail'),

    path('all-topics-documantation/', AllTopicsDocumentationListCreateAPIView.as_view(), name='all-topics-documantation-list'),
    path('all-topics-documantation/<int:pk>/', AllTopicsDocumentationRetrieveUpdateDestroyAPIView.as_view(), name='all-topics-documantation-detail'),

    path('test/', TestListCreateAPIView.as_view(), name='test-list'),
    path('test/<int:pk>/', TestRetrieveUpdateDestroyAPIView.as_view(), name='test-detail'),

    path('topics-test/', TopicsTestListCreateAPIView.as_view(), name='topics-test-list'),
    path('topics-test/<int:pk>/', TopicsTestRetrieveUpdateDestroyAPIView.as_view(), name='topics-test-detail'),

    path('about-us/', AboutUsListCreateAPIView.as_view(), name='about-us-list'),
    path('about-us/<int:pk>/', AboutUsRetrieveUpdateDestroyAPIView.as_view(), name='about-us-detail'),
]
