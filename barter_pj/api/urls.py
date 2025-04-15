from django.urls import path, include

from rest_framework.routers import SimpleRouter

from api.views import AdViewSet


app_name = 'api'

router_v1 = SimpleRouter()
router_v1.register('ads', AdViewSet, basename='ads')


urlpatterns = [
    path('', include(router_v1.urls)),
]
