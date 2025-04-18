from rest_framework.serializers import (ModelSerializer,
                                        ValidationError,
                                        )

from ad.models import Ad, Category, AdCategory


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name',)


class AdSerializer(ModelSerializer):
    category = CategorySerializer(
        many=True
    )

    class Meta:
        model = Ad
        fields = (
            'id', 'user', 'title',
            'description', 'image_url',
            'category', 'condition',
            'created_at',
        )
        read_only_fields = ('id', 'user')

    def validate(self, data):
        if (
            not self.partial and
            'category' in data and
            len(data.get('category')) == 0
        ):
            raise ValidationError(
                'Объявление не может быть без категории'
            )

        return data

    def set_category(self, ad, categories):
        for category in categories:
            current_category, _ = Category.objects.get_or_create(
                **category
            )
            AdCategory.objects.create(
                category=current_category,
                ad=ad
            )

    def create(self, validated_data):
        categories = validated_data.pop('category')
        ad = Ad.objects.create(**validated_data)
        self.set_category(ad, categories)
        return ad

    def update(self, instance, validated_data):
        categories = validated_data.pop('category', None)
        instance = super().update(instance, validated_data)
        if categories is None:
            instance.save()
            return instance
        instance.category.clear()
        self.set_category(instance, categories)
        instance.save()
        return instance
