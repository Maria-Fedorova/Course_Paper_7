# Generated by Django 5.1.4 on 2024-12-16 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Место выполнения привычки",
                    ),
                ),
                (
                    "start_time",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        verbose_name="Время начала выполнения привычки",
                    ),
                ),
                (
                    "action",
                    models.CharField(max_length=300, verbose_name="Действие привычки"),
                ),
                (
                    "is_pleasant",
                    models.BooleanField(
                        default=False, verbose_name="Признак приятной привычки"
                    ),
                ),
                (
                    "period_habit",
                    models.CharField(
                        choices=[
                            ("every day", "каждый день"),
                            ("every weak", "раз в неделю"),
                        ],
                        default="every day",
                        max_length=16,
                        verbose_name="Периодичность выполнения",
                    ),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True,
                        max_length=300,
                        null=True,
                        verbose_name="Вознаграждение",
                    ),
                ),
                (
                    "lead_time",
                    models.IntegerField(
                        default=1, verbose_name="Продолжительность выполнения привычки "
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(
                        default=False, verbose_name="Индикатор отправки"
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
                "ordering": ("id",),
            },
        ),
    ]