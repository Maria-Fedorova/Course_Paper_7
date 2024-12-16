from django.db import models

from users.models import User


class Habit(models.Model):
    PERIOD = [
        ("every day", "каждый день"),
        ("every weak", "раз в неделю")
    ]

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Владелец",
        blank=True,
        null=True,
    )
    location = models.CharField(
        max_length=100,
        verbose_name="Место выполнения привычки",
        blank=True,
        null=True,
    )
    start_time = models.DateTimeField(
        verbose_name="Время начала выполнения привычки",
        blank=True,
        null=True,
    )
    action = models.CharField(
        max_length=300,
        verbose_name="Действие привычки",
    )
    is_pleasant = models.BooleanField(
        default=False,
        verbose_name="Признак приятной привычки",
    )
    related_habit = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        verbose_name="Связанная привычка",
        blank=True,
        null=True,
    )
    period_habit = models.CharField(
        max_length=16,
        choices=PERIOD,
        verbose_name="Периодичность выполнения",
        default="every day",
    )
    reward = models.CharField(
        max_length=300,
        verbose_name="Вознаграждение",
        blank=True,
        null=True,
    )
    lead_time = models.IntegerField(
        default=1,
        verbose_name="Продолжительность выполнения привычки ",
    )

    STATUS_PUBLISHED = [
        ("Опубликован", "Опубликован"),
        ("Не опубликован", "Не опубликован"),
    ]

    is_published = models.BooleanField(
        default=False,
        verbose_name="Индикатор отправки",
    )

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        ordering = ("id",)

    def __str__(self):
        return self.habit
