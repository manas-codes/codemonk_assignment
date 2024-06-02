from rest_framework import serializers
from .models import Paragraph, WordIndex, CustomUser

#searlizer for paragraph creation
class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ['id', 'text', 'created_at', 'modified_at']

#serializers for text search
class WordIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordIndex
        fields = ['word', 'paragraph']

#serializers for user register
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'email', 'dob', 'created_at', 'modified_at']
