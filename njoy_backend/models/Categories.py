from django.db import models

class Categories(models.Model):
    title = models.CharField(max_length=32, blank=False, unique=True)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return f"{self.title}"