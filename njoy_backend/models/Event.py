from django.contrib.gis.db import models
from njoy_backend.models.User import User
from njoy_backend.models.Categories import Categories

class Event(models.Model):
    title = models.CharField(max_length=128, blank=False)
    owner = models.ForeignKey(User, verbose_name=("Owner"), on_delete=models.CASCADE, blank=False)
    date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False)
    category = models.ForeignKey(Categories, verbose_name=("Category"), on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    location = models.PointField(geography=True, blank=False, null=False)
     
    image = models.ImageField(upload_to="images/posters", height_field=None, width_field=None, max_length=None, blank=True)
    description = models.TextField(max_length=2048, blank=True)
    price = models.FloatField(default=0.0, blank=True)
    avaliable_places = models.IntegerField(default=0, blank=True)
    init_date = models.DateField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = ("Event")
        verbose_name_plural = ("Events")

    def __str__(self):
        return f"{self.title}"
