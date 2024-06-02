from django.urls import path
from .views import ParagraphCreate, ParagraphSearch, UserRegister, UserLogin

urlpatterns = [
    path('register/', UserRegister.as_view(), name='user-register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('paragraph/', ParagraphCreate.as_view(), name='paragraph-create'),
    path('search/', ParagraphSearch.as_view(), name='paragraph-search'),
]
