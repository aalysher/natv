from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.models import Channel, Discount, Price
from core.serializers import ChannelSerializer, OrderSerializer

from .dto import get_channels_dto


@api_view(['GET', 'POST'])
def get_channels(request):
    if request.method == 'GET':
        channels = Channel.objects.filter(active=True)
        channels_dto = get_channels_dto(channels)
        serializer = ChannelSerializer(channels_dto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
