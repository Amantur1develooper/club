from rest_framework import generics, permissions
from core.models import User, Documentation, Topics_Documentation, Test, Topics_Test, AboutUs, All_Topics_Documentation
from core.api.serializers import UserSerializer, DocumentationSerializer, TopicsDocumentationSerializer, TestSerializer, \
    TopicsTestSerializer, AboutUsSerializer, AllTopicsDocumentationSerializer


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class DocumentationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Documentation.objects.all()
    serializer_class = DocumentationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DocumentationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Documentation.objects.all()
    serializer_class = DocumentationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TopicsDocumentationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Topics_Documentation.objects.all()
    serializer_class = TopicsDocumentationSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]


class TopicsDocumentationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topics_Documentation.objects.all()
    serializer_class = TopicsDocumentationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AllTopicsDocumentationListCreateAPIView(generics.ListCreateAPIView):
    queryset = All_Topics_Documentation.objects.all()
    serializer_class = AllTopicsDocumentationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AllTopicsDocumentationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = All_Topics_Documentation.objects.all()
    serializer_class = AllTopicsDocumentationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TestListCreateAPIView(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TestRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TopicsTestListCreateAPIView(generics.ListCreateAPIView):
    queryset = Topics_Test.objects.all()
    serializer_class = TopicsTestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TopicsTestRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topics_Test.objects.all()
    serializer_class = TopicsTestSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]


class AboutUsListCreateAPIView(generics.ListCreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AboutUsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
