from django.contrib.auth.models import User
from rest_framework import serializers

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""

        request = self.context.get('request')
        if request and request.user.is_authenticated:
            # При обновлении не проверяем, если не меняем статус на OPEN
            if self.instance:
                old_status = self.instance.status
                new_status = data.get('status', old_status)
                if new_status != 'OPEN':
                    return data
            open_count = request.user.advertisement_set.filter(status='OPEN').count()
            if open_count >= 10:
                raise serializers.ValidationError(
                    {'detail': 'У вас уже есть 10 открытых объявлений.'}
                )

        return data
