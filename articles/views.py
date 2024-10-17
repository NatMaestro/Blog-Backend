import itertools
from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer
# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsAuthor
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from django.utils.text import slugify

class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all().order_by("-created_at")
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        base_slug = slugify(title)
        slug = base_slug

        # Ensure the slug is unique
        for x in itertools.count(1):
            if not Article.objects.filter(slug=slug).exists():
                break
            slug = f"{base_slug}-{x}"

        # Save the article, using the author from the validated data
        serializer.save(slug=slug)  # `author` will be saved as-is from the request data
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({"error": "An article with this slug already exists."}, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    lookup_field = 'slug'  # Add this line to specify the lookup field
    # permission_classes = [IsAuthor]

    def get_queryset(self):
        return Article.objects.all()

    def retrieve(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        try:
            article = self.get_queryset().get(slug=slug)
            serializer = self.get_serializer(article)
            return Response(serializer.data)
        except Article.DoesNotExist:
            return Response({"error": "Article not found."}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        try:
            article = self.get_queryset().get(slug=slug)
            serializer = self.get_serializer(article, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        except Article.DoesNotExist:
            return Response({"error": "Article not found."}, status=status.HTTP_404_NOT_FOUND)
        except IntegrityError:
            return Response({"error": "An article with this slug already exists."}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        try:
            article = self.get_queryset().get(slug=slug)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Article.DoesNotExist:
            return Response({"error": "Article not found."}, status=status.HTTP_404_NOT_FOUND)

