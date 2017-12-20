from django.db import models


class Channel(models.Model):

    name = models.CharField(max_length=50)
    father = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Channel"
        verbose_name_plural = "Channels"

    def __str__(self):
        return self.name


class Category(models.Model):

    name = models.CharField(max_length=50)
    channel = models.ForeignKey(
        Channel,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"

    def __str__(self):
        return self.name
