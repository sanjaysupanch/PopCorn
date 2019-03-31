from django.db import models
from datetime import datetime
from Celebrities.models import Celebrities
from django.utils import timezone


class Show(models.Model):
    Movie_title = models.CharField(max_length=200, db_index=True)
    ReleaseDate = models.DateField(db_index=True, default=timezone.now)
    Duration = models.IntegerField()
    Description = models.TextField(max_length=2000)
    Cast = models.ManyToManyField(Celebrities, related_name="cast")
    GENRE_CHOICES = (
        ('R', 'Romance'),
        ('C', 'Comedy'),
        ('T', 'Thriller'),
        ('S', 'Sci-Fi'),
        ('D', 'Drama'),
        ('A', 'Action')
    )
    Genre = models.CharField(max_length=1, choices=GENRE_CHOICES)
    Country = models.CharField(max_length=200)
    Budget = models.IntegerField(default=0)
    Boc = models.IntegerField(db_index=True)
    STATUS_CHOICE = (
        ('F', 'Flop'),
        ('L', 'Losing'),
        ('A', 'Average'),
        ('H', 'Hit'),
        ('S', 'SuperHit'),
        ('B', 'Blockbuster'),
        ('R', 'Running')
    )
    Avg_rating = models.FloatField(blank=True, db_index=True, default=0.0)
    Num_ratings = models.IntegerField(blank=True, default=0)
    Status = models.CharField(max_length=1, choices=STATUS_CHOICE, null=True, blank=True)
    Trailer = models.CharField(max_length=2000, null=True, blank=True)
    SHOW_TYPE = (
        ('tv', 'tvseries'),
        ('m', 'movies'),
    )
    type = models.CharField(max_length=2, choices=SHOW_TYPE)


class SEASON(models.Model):
    Season_title = models.CharField(max_length=200, null=True, blank=True)
    ReleaseDate = models.DateField(db_index=True, default=timezone.now)
    Series = models.ForeignKey(Show, on_delete=models.CASCADE, null=True, blank=True)


class EPISODE(models.Model):
    Episode_title = models.CharField(max_length=200, null=True, blank=True)
    Duration = models.IntegerField(null=True, blank=True)
    Season = models.ForeignKey(SEASON, on_delete=models.CASCADE, null=True, blank=True)



