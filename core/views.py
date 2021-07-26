from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination

from core.models import Channel
from core.serializers import ChannelSerializer, OrderSerializer

from .dto import get_channels_dto


class ChannelList(generics.ListCreateAPIView):
    queryset = get_channels_dto()
    pagination_class = LimitOffsetPagination

    def get(self, request, *args, **kwargs):
        ChannelList.serializer_class = ChannelSerializer
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        ChannelList.serializer_class = OrderSerializer
        return self.create(request, *args, **kwargs)
