from .models import Article, Comment, Movie, UserChoice
from rest_framework import serializers
from accounts.serializers import UserSerializer

# Movie 

class MovieSerializer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    fields = ['id']

class MovieListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    fields = ['id', 'title', 'summary', 'Audience_score', 'country', 'Release_date', 'Showtimes', 'movie_director', 'Actors',
    'Rating', 'imgUrl', 'content', 'heart', 'Screening', 'attendance', 'like_users', 'still_img', 'people']

class MovieDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    fields = ['id', 'title', 'summary', 'Audience_score', 'country', 'Release_date', 'Showtimes', 'movie_director', 'Actors',
    'Rating', 'imgUrl', 'content', 'heart', 'Screening', 'attendance', 'like_users', 'still_img', 'people']

# Article

class ArticleSerializer(serializers.ModelSerializer):
  user = UserSerializer(required=False)
  movie = MovieListSerializer(required=False)
  class Meta:
    model = Article
    fields = ['id', 'title', 'content', 'user', 'movie', 'created_at', 'updated_at', 'Rank', 'like_users']

class ArticleListSerializer(serializers.ModelSerializer):
  user = UserSerializer()
  class Meta:
    model = Article
    fields = ['id', 'title', 'content', 'user', 'created_at', 'updated_at', 'Rank', 'like_users']

# Comment

class CommentListSerializer(serializers.ModelSerializer):
  user = UserSerializer()
  article = ArticleListSerializer()
  class Meta:
    model = Comment
    fields = ['id', 'content', 'user', 'article']

class CommentSerializer(serializers.ModelSerializer):
  user = UserSerializer(required=False)
  article = ArticleListSerializer(required=False)
  class Meta:
    model = Comment
    fields = ['id', 'content', 'user', 'article']

# userForm
class UserChoiceSerializer(serializers.ModelSerializer):
  user = UserSerializer(required=False)
  class Meta:
    model = UserChoice
    fields = ['gender', 'drama', 'fear', 'melloh', 'thriller', 'comedey', 'animation', 'suspense', 'action', 'sf', 'age',
      'kids', 'parent_F', 'parent_M', 'Favorite', 'user']

class UserChoiceListSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserChoice
    fields = ['gender', 'drama', 'fear', 'melloh', 'thriller', 'comedey', 'animation', 'suspense', 'action', 'sf', 'age',
      'kids', 'parent_F', 'parent_M', 'Favorite', 'id']