from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from ad.models import Ad

from api.serializers import AdSerializer


class AdViewSet(ModelViewSet):
    """Вьюсет с круд операциями для объявлений"""

    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [AllowAny,]
