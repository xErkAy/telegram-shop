from django.db import models


class User(models.Model):
    user_id = models.BigIntegerField(primary_key=True, verbose_name="ID пользователя")
    user_name = models.TextField(verbose_name="@ пользователя", max_length=40)
    first_name = models.TextField(verbose_name="Имя пользователя", null=True, max_length=40)
    is_order_active = models.BooleanField(verbose_name="Сбор данных по заказу", default=False)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Order(models.Model):
    order_id = models.AutoField(primary_key=True, verbose_name="ID заказа")
    user_id = models.ForeignKey("User", verbose_name="ID пользователя", on_delete=models.CASCADE)
    order_value = models.CharField(max_length=200, verbose_name="Содержимое заказа")
    status = models.SmallIntegerField(verbose_name="Статус заказа")
    is_closed = models.BooleanField(verbose_name="Заказ выполнен", default=False)
    date = models.DateTimeField(verbose_name="Дата и время заказа", auto_now_add=True)
    is_chat_active = models.BooleanField(verbose_name="Активная переписка", default=False)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class Message(models.Model):
    message_id = models.BigAutoField(primary_key=True, verbose_name="ID сообщения")
    user_id = models.ForeignKey("User", verbose_name="ID пользователя", on_delete=models.CASCADE)
    order_id = models.ForeignKey("Order", verbose_name="ID заказа", on_delete=models.CASCADE)
    message_text = models.CharField(max_length=200, verbose_name="Текст сообщения")
    is_sender = models.BooleanField(verbose_name="Является ли пользователь отправителем?")
    date = models.DateTimeField(verbose_name="Дата и время отправки", auto_now_add=True)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
