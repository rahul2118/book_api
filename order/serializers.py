from rest_framework import serializers
from .models import Order, User, Book
from user.serializers import UserSerializer
from product.serializers import BookSerializer


# class OrderSerializer(serializers.ModelSerializer):
#     user = UserSerializer(many=True, read_only=True)
#     products = BookSerializer(many=True, read_only=True)

#     class Meta:
#         model = Order
#         fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        source='user', queryset=User.objects.all(), write_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        user = validated_data.pop('user')
        validated_data['user_id'] = user.id
        order = super().create(validated_data)
        return order
