from .models import Channel, Price, Discount


class ChannelDto:
    pass


def get_channels_dto(channels):
    channels_list = []
    for channel in channels:
        channel_instance = ChannelDto()
        channel_instance.id = channel.id
        channel_instance.name = channel.name
        channel_instance.image = channel.photo
        channel_instance.price = Price.objects.get(channel=channel).price
        channel_instance.discount = Discount.objects.filter(channel=channel)
        channels_list.append(channel_instance)
    return channels_list
