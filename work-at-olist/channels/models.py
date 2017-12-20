from django.db import models


class Channel(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Channel"
        verbose_name_plural = "Channels"

    def __str__(self):
        return self.name


class Category(models.Model):

    name = models.CharField(max_length=50)
    parent_category = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='sub_categories',
        blank=True,
        null=True
    )

    channel = models.ForeignKey(
        Channel,
        on_delete=models.CASCADE,
        default=True
    )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"

    def save(self):
        parent_category = self.parent_category
        if parent_category:
            self.channel = parent_category.channel
            print(self.channel)

        super(Category, self).save()

    def __str__(self):
        return self.name
