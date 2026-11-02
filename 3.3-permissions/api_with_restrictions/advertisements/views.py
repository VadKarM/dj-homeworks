from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import PermissionDenied

from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from advertisements.filters import AdvertisementFilter
from django_filters.rest_framework import DjangoFilterBackend


class IsOwnerOrAdmin(BasePermission):
    """Разрешение только для автора объявления или админа."""

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return obj.creator == request.user


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ['create', 'update', 'partial_update']:
            return [IsAuthenticated()]
        return []

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if not IsOwnerOrAdmin().has_object_permission(request, self, instance):
            raise PermissionDenied('У вас нет прав на удаление этого объявления.')
        return super().destroy(request, *args, **kwargs)
