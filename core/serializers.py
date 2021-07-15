from rest_framework import serializers

from .models import Channel, Discount, Order


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ('min_days', 'percent')


class ChannelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    photo = serializers.ImageField(required=False)
    price = serializers.FloatField()
    discount = DiscountSerializer(many=True)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class Dayserializer(serializers.Serializer):
    day = serializers.CharField(max_length=255, required=False)


class ChannelPostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    price = serializers.IntegerField()
    day = Dayserializer(many=True)


class OrderDetailSerializer(serializers.Serializer):
    order = OrderSerializer(many=True, required=False)
    channel = ChannelPostSerializer(many=True)
