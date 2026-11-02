from django_filters import rest_framework as filters

from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = filters.DateFromToRangeFilter(field_name='created_at__date')
    status = filters.ChoiceFilter(choices=AdvertisementStatusChoices.choices)
    creator = filters.NumberFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status', 'creator']
