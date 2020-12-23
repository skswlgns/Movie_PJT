from django.db import models
from django.conf import settings


class Movie(models.Model):
  title = models.CharField(max_length=50)
  summary = models.CharField(max_length=50)
  Audience_score = models.FloatField()
  country = models.CharField(max_length=20)
  Release_date = models.CharField(max_length=20)
  Showtimes = models.CharField(max_length=10)
  movie_director = models.CharField(max_length=10)
  Actors = models.CharField(max_length=50)
  Rating = models.CharField(max_length=15)
  imgUrl = models.CharField(max_length=100)
  content = models.TextField()
  heart = models.IntegerField()
  Screening = models.CharField(max_length=10)
  people = models.IntegerField()
  attendance = models.CharField(max_length=30)
  still_img = models.CharField(max_length=150)

  like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)

class Article(models.Model):
  title = models.CharField(max_length=70)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  Rank = models.IntegerField()
  
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)

class Comment(models.Model):
  content = models.TextField()
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments', blank=True)

class UserChoice(models.Model):
  gender = models.CharField(max_length=5)

  drama = models.BooleanField(default=False)
  fear = models.BooleanField(default=False)
  melloh = models.BooleanField(default=False)
  thriller = models.BooleanField(default=False)
  comedey = models.BooleanField(default=False)
  animation = models.BooleanField(default=False)
  suspense = models.BooleanField(default=False)
  action = models.BooleanField(default=False)
  sf = models.BooleanField(default=False)

  age = models.IntegerField()
  kids = models.BooleanField(default=False)

  parent_F = models.IntegerField()
  parent_M = models.IntegerField()

  Favorite = models.CharField(max_length=10)

  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


