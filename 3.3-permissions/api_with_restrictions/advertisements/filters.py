from django_filters import rest_framework as filters

from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    created_at_after = filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    created_at_before = filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')
    status = filters.ChoiceFilter(choices=AdvertisementStatusChoices.choices)
    creator = filters.NumberFilter(field_name='creator__id')

    class Meta:
        model = Advertisement
        fields = ['created_at_after', 'created_at_before', 'status', 'creator']
