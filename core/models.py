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

    def __str__(self):
        return self.name


class Price(models.Model):
    """Цены каналов"""
    price = models.FloatField("Цена")
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(default=datetime(2999, 12, 31))
    channel = models.ForeignKey(Channel,
                                on_delete=models.DO_NOTHING)

    # def __str__(self):
    #     return self.price


class Discount(models.Model):
    """Скидки"""
    min_days = models.IntegerField("Минимальное количество дней")
    percent = models.IntegerField('Процент скидки')
    channel = models.ForeignKey(Channel,
                                on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(default=datetime(2999, 12, 31))

    def __str__(self):
        return str(self.channel)


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

    def __str__(self):
        return self.name


class OrderDetail(models.Model):
    """Детали операции"""
    order = models.ForeignKey(Order,
                              on_delete=models.DO_NOTHING)
    channel = models.ForeignKey(Channel,
                                on_delete=models.DO_NOTHING)
    price = models.FloatField()

    def __str__(self):
        return str(self.order)


class Day(models.Model):
    order = models.ForeignKey(OrderDetail,
                              on_delete=models.DO_NOTHING)
    day = models.DateField()

