from django.contrib import admin

from core.models import Channel, Discount, \
    Price, Order, OrderDetail, Day


class ChannelSettings(admin.ModelAdmin):
    list_display = ('id', 'name', 'active', 'order_num')


class OrderSettings(admin.ModelAdmin):
    list_display = ('id', 'name', 'total_price', 'status')


class OrderDetailSettings(admin.ModelAdmin):
    list_display = ('order', 'channel', 'price')


class DaySettings(admin.ModelAdmin):
    list_display = ('order', 'day')


admin.site.register(Channel, ChannelSettings)
admin.site.register(Discount)
admin.site.register(Price)
admin.site.register(Order, OrderSettings)
admin.site.register(OrderDetail, OrderDetailSettings)
admin.site.register(Day, DaySettings)
