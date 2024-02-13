from rest_framework import serializers
from .models import Items, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    category_id = CategorySerializer()

    class Meta:
        model = Items
        fields = '__all__'
        depth =  1  # To handle nested serialization

    def create(self, validated_data):
        category_data = validated_data.pop('category_id')
        category = CategorySerializer.create(CategorySerializer(), validated_data=category_data)
        item = Items.objects.create(category_id=category, **validated_data)
        return item
