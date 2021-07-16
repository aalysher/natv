from datetime import datetime

from rest_framework import serializers

from .models import Channel, Discount, Order, OrderDetail, Day


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



class ChannelPostSerializer(serializers.Serializer):
    channel_id = serializers.IntegerField()
    price = serializers.IntegerField()
    days = serializers.ListField()


class OrderSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)
    phone = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)
    total_price = serializers.CharField(max_length=255)
    channels = ChannelPostSerializer(many=True, required=False)

    def create(self, validated_data):
        order = Order.objects.create(text=validated_data['text'],
                                     name=validated_data['name'],
                                     phone=validated_data['phone'],
                                     email=validated_data['email'],
                                     total_price=validated_data['total_price']
                                     )

        for i in validated_data['channels']:
            channel = Channel.objects.get(pk=i['channel_id'])
            ord_detail = OrderDetail.objects.create(
                channel=channel,
                order=order,
                price=i['price']
            )

            for day in i['days']:
                day = Day.objects.create(
                    day=datetime(2021, 1, 1),
                    order=ord_detail
                )
        return order

