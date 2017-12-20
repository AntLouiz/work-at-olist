from django.db import models
from django.utils.text import slugify


class Channel(models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name = "Channel"
        verbose_name_plural = "Channels"

    def save(self):
        self.slug = slugify(self.name)
        super(Channel, self).save()

    def __str__(self):
        return self.name


class Category(models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True)
    parent_category = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='categories',
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

        self.slug = slugify(self.name)
        super(Category, self).save()

    def __str__(self):
        return self.name
