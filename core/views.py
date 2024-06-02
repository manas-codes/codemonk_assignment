from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Paragraph, WordIndex, CustomUser
from .serializers import ParagraphSerializer, CustomUserSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
import string
User = get_user_model()

#paragraph creation endpoint 
class ParagraphCreate(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        paragraphs = request.data.get('text', '').split('\n\n')
        created_paragraphs = []
        for paragraph_text in paragraphs:
            paragraph = Paragraph.objects.create(text=paragraph_text.strip())
            self.index_words(paragraph)
            created_paragraphs.append(paragraph)

        serializer = ParagraphSerializer(created_paragraphs, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    #breakdown of words in paragraph
    def index_words(self, paragraph):
        translator = str.maketrans('', '', string.punctuation) 
        words = paragraph.text.split()
        for word in words:
            cleaned_word = word.lower().translate(translator)  
            if cleaned_word: 
                WordIndex.objects.create(word=cleaned_word, paragraph=paragraph)

#Text search endpoint
class ParagraphSearch(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        word = request.data.get('word', '').lower()
        paragraphs = WordIndex.objects.filter(word=word).values_list('paragraph', flat=True).distinct()
        results = Paragraph.objects.filter(id__in=paragraphs)[:10]
        serializer = ParagraphSerializer(results, many=True)
        return Response(serializer.data)

#User register endpoint
class UserRegister(APIView):
    def post(self, request, format=None):
        email = request.data.get('email')
        name = request.data.get('name')
        dob = request.data.get('dob')
        password = request.data.get('password')
        user = User.objects.create_user(email=email, name=name, dob=dob, password=password)
        return Response({
            'message': 'User created successfully',
        }, status=status.HTTP_201_CREATED)

#User login endpoint
class UserLogin(APIView):
    def post(self, request, format=None):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            raise AuthenticationFailed('Invalid login credentials')