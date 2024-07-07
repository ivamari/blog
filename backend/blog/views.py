from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets, filters

from .models import Post
from .serializers import PostSerializer
from rest_framework.pagination import PageNumberPagination


@extend_schema_view(
    list=extend_schema(summary='Список постов', tags=['Посты']),
    retrieve=extend_schema(summary='Деталка поста',
                           tags=['Посты']),
    update=extend_schema(summary='Обновить пост',
                         tags=['Посты']),
    create=extend_schema(summary='Создать пост',
                         tags=['Посты']),
    destroy=extend_schema(summary='Удалить пост',
                          tags=['Посты']),
)
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('title', 'content')
