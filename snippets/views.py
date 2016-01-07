from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User

class SnippetList(generics.ListCreateAPIView):
	queryset = Snippet.objects.all()
	serializers_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Snippet.objects.all()
	serializers_class = SnippetSerializer

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializers_class = UserSerializer

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializers_class = UserSerializer