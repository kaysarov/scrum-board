from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import user_passes_test


class Sprint(models.Model):
    title = models.CharField("Название", max_length=100, blank=True, default='')
    description = models.TextField("Описание", blank=True, default='')
    begin = models.DateField("Начало", unique=True)
    end = models.DateField("Конец", unique=True)

    class Meta:
        verbose_name = "Спринт"
        verbose_name_plural = "Спринты"

    def __str__(self):
        return self.title or _('Sprint заканчивается %s') % self.end


class Task(models.Model):
    STATUS_TODO = 1
    STATUS_IN_PROGRESS = 2
    STATUS_TESTING = 3
    STATUS_DONE = 4

    STATUS_CHOICES = (
        (STATUS_TODO, _('Запланировано')),
        (STATUS_IN_PROGRESS, _('В работе')),
        (STATUS_TESTING, _('Тестирование')),
        (STATUS_DONE, _('Готово')),
    )

    PRIORITY_1 = 1
    PRIORITY_2 = 2
    PRIORITY_3 = 3

    PRIORITY_CHOICES = (
        (PRIORITY_1, _('Высокий')),
        (PRIORITY_2, _('Средний')),
        (PRIORITY_3, _('Низкий')),
    )

    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание", blank=True, default='')
    sprint = models.ForeignKey(Sprint, verbose_name="Спринт", blank=True, null=True, on_delete=models.CASCADE)
    status = models.SmallIntegerField("Статус", choices=STATUS_CHOICES, default=STATUS_TODO)
    priority = models.SmallIntegerField("Приоритет", choices=PRIORITY_CHOICES)
    assigned = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Исполнитель", null=True, blank=True, on_delete=models.CASCADE)
    done = models.DateField("Изменение", blank=True, auto_now_add=True)

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.title


def group_required(*group_names):
    def in_groups(user):
        if user.is_superuser or bool(user.groups.filter(name__in=group_names)):
            return True
        return False
    return user_passes_test(in_groups)
