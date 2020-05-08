from django.db import models


# Create your models here.

class Games(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=120, blank=False, default='')
    game_category = models.CharField(max_length=100, blank=False, default='')
    description = models.CharField(max_length=250, blank=True, default='')
    release_date = models.DateTimeField()
    was_included_in_home = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)
