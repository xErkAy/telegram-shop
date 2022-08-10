from django.db import models


class Users(models.Model):
    user_id = models.IntegerField(primary_key=True, verbose_name="ID пользователя")
    user_name = models.TextField(verbose_name="@ пользователя", max_length=40)
    first_name = models.TextField(verbose_name="Имя пользователя", null=True, max_length=40)

    def __str__(self):
        return f'[{self.user_name}] {self.first_name}'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class Orders(models.Model):
    order_id = models.IntegerField(primary_key=True, verbose_name="ID заказа")
    user_id = models.ForeignKey("Users", verbose_name="ID пользователя", on_delete=models.CASCADE)
    order_value = models.CharField(max_length=200, verbose_name="Заказ")
    status = models.SmallIntegerField(verbose_name="Статус заказа")
    is_closed = models.BooleanField(verbose_name="Заказ выполнен")
    date = models.DateTimeField(verbose_name="Дата и время заказа", auto_now=True)

    def __str__(self):
        return f'[{self.user_id.user_name}] Заказ №{self.order_id}'

    @property
    def get_user(self):
        return {
            "user_id": self.user_id.user_id,
            "user_name": self.user_id.user_name,
            "first_name": self.user_id.first_name
        }

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

class Messages(models.Model):
    user_id = models.ForeignKey("Users", verbose_name="ID пользователя", on_delete=models.CASCADE)
    order_id = models.ForeignKey("Orders", verbose_name="ID заказа", on_delete=models.CASCADE)
    message_text = models.CharField(max_length=200, verbose_name="Текст сообщения")
    is_sender = models.BooleanField(verbose_name="Является ли пользователь отправителем?")
    is_read = models.BooleanField(verbose_name="Сообщение прочитано?")
    date = models.DateTimeField(verbose_name="Дата и время отправки", auto_now=True)

    def __str__(self):
        return f'{self.user_id} {self.message_text}'

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
