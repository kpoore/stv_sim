from __future__ import unicode_literals

from django.db import models
import os

def get_image_path(filename, instance):
    return os.path.join('images', str(instance.id), filename)

# Create your models here.
class Choice(models.Model):
    descript = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.descript


class Ballot(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    choice_picture = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    order = models.PositiveSmallIntegerField(default=1)
    votes = models.IntegerField(default=0)
    first_vote = models.IntegerField(default=0)
    second_vote = models.IntegerField(default=0)
    third_vote = models.IntegerField(default=0)
