from rest_framework import serializers
from core.models import User, Documentation, Topics_Documentation, Test, Topics_Test, AboutUs, All_Topics_Documentation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Этот email уже занят.")
        return value


class DocumentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documentation
        fields = '__all__'

    def validate(self, data):
        if not data.get('description'):
            raise serializers.ValidationError("Поле 'description' не может быть пустым.")
        return data


class TopicsDocumentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topics_Documentation
        fields = '__all__'


class AllTopicsDocumentationSerializer(serializers.ModelSerializer):

    class Meta:
        model = All_Topics_Documentation
        fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class TopicsTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topics_Test
        fields = '__all__'


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'
