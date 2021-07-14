from datetime import datetime

from django.db import models


class Channel(models.Model):
    """Канал"""
    name = models.CharField("Название канала:",
                            max_length=255)
    photo = models.ImageField("Лого канала",
                              upload_to='Images',
                              blank=True,
                              null=True)
    active = models.BooleanField("Активен",
                                 default=True)

    order_num = models.IntegerField("Приоритет по фильтрации")


class Price(models.Model):
    """Цены каналов"""
    price = models.FloatField("Цена")
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(default=datetime(2999, 12, 31))
    channel_id = models.ForeignKey(Channel,
                                   on_delete=models.DO_NOTHING)


class Discount(models.Model):
    """Скидки"""
    min_days = models.IntegerField("Минимальное количество дней")
    percent = models.IntegerField('Процент скидки')
    channel_id = models.ForeignKey(Channel,
                                   on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(default=datetime(2999, 12, 31))


statuses = (('Open', 'Открыт'), ('Paid', 'Оплачен'), ('Closed', 'Закрыт'))


class Order(models.Model):
    """Операция"""
    add_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField("Текст заказа")
    name = models.CharField("Имя клиента",
                            max_length=255)
    phone = models.CharField("Номер телефона клиента",
                             max_length=255)
    email = models.CharField("Почта",
                             max_length=255)
    total_price = models.FloatField()
    edit_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255,
                              choices=statuses,
                              default='Open')


class OrderDetail(models.Model):
    """Детали операции"""
    order_id = models.ForeignKey(Order,
                                 on_delete=models.DO_NOTHING)
    channel_id = models.ForeignKey(Channel,
                                   on_delete=models.DO_NOTHING)
    price = models.FloatField()


class Day(models.Model):
    order_detail_id = models.ForeignKey(OrderDetail,
                                        on_delete=models.DO_NOTHING)
    day = models.DateField()
