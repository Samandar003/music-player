from django.db import models


class Song(models.Model):
    title= models.CharField(max_length=100)
    artist= models.CharField(max_length=100)
    image= models.ImageField()
    audio_file = models.FileField(blank=True,null=True)
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    duration=models.PositiveSmallIntegerField()
    paginate_by = 2

    def __str__(self):
        return self.title

