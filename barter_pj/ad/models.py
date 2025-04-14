from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


CHOICES = (
    ('Waiting', 'Ожидает'),
    ('Accepted', 'Принята'),
    ('Declined', 'Отклонена')
)


class Category(models.Model):
    """Модель категорий"""

    name = models.CharField(
        'Название категории',
        max_length=50
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Ad(models.Model):
    """Модель объявления"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='ad',
        verbose_name='Автор объявления'
    )
    title = models.CharField(
        'Заголовок объявления',
        max_length=50
    )
    description = models.TextField(
        'Описание товара'
    )
    image_url = models.ImageField(
        upload_to='media/',
        verbose_name='URL изображения',
        blank=True
    )
    category = models.ManyToManyField(
        Category,
        through='AdCategory',
        related_name='ad',
        verbose_name='Категория товара'
    )
    condition = models.CharField(
        'Состояние товара',
        max_length=50,
    )
    created_at = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )

    class Meta:

        verbose_name = 'объявление'
        verbose_name_plural = 'Объявления'


class ExchangeProposal(models.Model):
    """Модель для предложения обмена"""

    ad_sender = models.ForeignKey(
        Ad,
        verbose_name='Объявление-инициатор',
        on_delete=models.CASCADE,
        related_name='sender'
    )
    ad_recive = models.ForeignKey(
        Ad,
        verbose_name='Объявление-получатель',
        on_delete=models.CASCADE,
        related_name='recive'
    )
    comment = models.TextField(
        'Комментарий к предложению'
    )
    status = models.CharField(
        'Статус предложения',
        choices=CHOICES,
        default='Waiting'
    )

    class Meta:
        verbose_name = 'предложение'
        verbose_name_plural = 'Предложения'


class AdCategory(models.Model):
    """Промежуточная таблица объявления и категорий"""

    ad = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE,
        related_name='ad_category'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ad_category'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('ad', 'category'),
                name='adcategory_unique'
            )
        ]
        verbose_name = 'категория объявления'
        verbose_name_plural = 'Категории объявлений'
