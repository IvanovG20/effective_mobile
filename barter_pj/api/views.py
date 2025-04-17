from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

from django_filters.rest_framework import DjangoFilterBackend

from ad.models import Ad

from api.serializers import AdSerializer
from api.permissions import AuthorOrReadOnly


class AdViewSet(ModelViewSet):
    """Вьюсет с круд операциями для объявлений"""

    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [AuthorOrReadOnly,]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('category', 'condition')
    search_fields = ('title', 'description')
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
