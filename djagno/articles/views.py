from django.shortcuts import render, get_object_or_404
from .models import Article, Comment, Movie, UserChoice
from .serializers import ArticleSerializer, ArticleListSerializer, MovieListSerializer, MovieDetailSerializer
from .serializers import CommentSerializer, CommentListSerializer, UserChoiceSerializer, UserChoiceListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


# movie

@api_view(['GET'])
def movie(request):
  movies = Movie.objects.order_by('pk')
  serializer = MovieListSerializer(movies, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
  movie = get_object_or_404(Movie, pk=movie_pk)
  serializer = MovieDetailSerializer(movie)
  return Response(serializer.data)

# Article

@api_view(['GET'])
def article(request, movie_pk, article_pk):
  article = get_object_or_404(Article, pk=article_pk)
  serializer = ArticleListSerializer(article)
  return Response(serializer.data)

@api_view(['GET'])
def article_list(request, movie_pk):
  movie = get_object_or_404(Movie, pk=movie_pk)
  article = movie.article_set.order_by('-pk')
  serializer = ArticleListSerializer(article, many=True)
  return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def article_create(request, movie_pk):
  movie = get_object_or_404(Movie, pk=movie_pk)
  serializer = ArticleSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    serializer.save(user=request.user, movie=movie)

    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def article_delete(request, movie_pk, article_pk):
  article = get_object_or_404(Article, pk=article_pk)
  moive = get_object_or_404(Movie, pk=movie_pk)
  if article.user == request.user:
    article.delete()
    return Response('성공적으로 삭제되었습니다.')
  else:
    return Response({"detail": "본인이 작성한 글만 삭제 할 수 있습니다."})
  
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def article_update(request, movie_pk, article_pk):
  article = get_object_or_404(Article, pk=article_pk)
  moive = get_object_or_404(Movie, pk=movie_pk)
  if article.user == request.user:
    serializer = ArticleSerializer(article, data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data)
  else:
    return Response({"detail": "본인이 작성한 글만 수정 할 수 있습니다."})


# Comment

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, movie_pk, article_pk):
  movie = get_object_or_404(Movie, pk=movie_pk)
  article = get_object_or_404(Article, pk=article_pk)
  serializer = CommentSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    serializer.save(user=request.user, article=article)

    return Response(serializer.data)

@api_view(['GET'])
def comment_list(request, movie_pk, article_pk):
  comments = Comment.objects.filter(article_id=article_pk).order_by('-pk')
  movie = get_object_or_404(Movie, pk=movie_pk)
  article = get_object_or_404(Article, pk=article_pk)
  serializer = CommentListSerializer(comments, many=True)
  return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_delete(request, movie_pk, article_pk, comment_pk):
  article = get_object_or_404(Article, pk=article_pk)
  moive = get_object_or_404(Movie, pk=movie_pk)
  comment = get_object_or_404(Comment, pk=comment_pk)
  if comment.user == request.user:
    comment.delete()
    return Response('성공적으로 삭제되었습니다.')
  else:
    return Response({"detail": "본인이 작성한 댓글만 삭제 할 수 있습니다."})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_update(request, movie_pk, article_pk, comment_pk):
  article = get_object_or_404(Article, pk=article_pk)
  moive = get_object_or_404(Movie, pk=movie_pk)
  comment = get_object_or_404(Comment, pk=comment_pk)
  if comment.user == request.user:
    serializer = CommentSerializer(comment, data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data)
  else:
    return Response({"detail": "본인이 작성한 글만 수정 할 수 있습니다."})

# heart

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_heart(request, movie_pk):
  movie = get_object_or_404(Movie, pk=movie_pk)
  if movie.like_users.filter(id=request.user.pk).exists():
      movie.heart -= 1
      movie.save()
      movie.like_users.remove(request.user)
  else:
      movie.heart += 1
      movie.save()
      movie.like_users.add(request.user)
  serializer = MovieDetailSerializer(movie)
  return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def article_thumb(request, article_pk):
  article = get_object_or_404(Article, pk=article_pk)
  if article.like_users.filter(id=request.user.pk).exists():
      article.like_users.remove(request.user)
  else:
      article.like_users.add(request.user)
  serializer = ArticleSerializer(article)
  return Response(serializer.data)

@api_view(['GET'])
def people(request):
  movies = Movie.objects.order_by('-people')[:10]
  serializer = MovieListSerializer(movies, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def heart(request):
  movies = Movie.objects.order_by('-heart')[:10]
  serializer = MovieListSerializer(movies, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def score(request):
  movies = Movie.objects.order_by('-Audience_score')[:10]
  serializer = MovieListSerializer(movies, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def now(request):
  movies = Movie.objects.filter(Screening='상영중').order_by('?')[:10]
  serializer = MovieListSerializer(movies, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def cry(request):
  movies = Movie.objects.filter(summary__contains='코미디').order_by('?')[:10]
  serializer = MovieListSerializer(movies, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def melloh(request):
  movies = Movie.objects.filter(summary__contains='멜로').order_by('?')[:10]
  serializer = MovieListSerializer(movies, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def thriller(request):
  movies = Movie.objects.filter(Q(summary__contains='스릴러') | Q(summary__contains='공포')).order_by('?')[:10]
  serializer = MovieListSerializer(movies, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def angry(request):
  movies = Movie.objects.filter(Q(summary__contains='액션') | Q(summary__contains='SF')).order_by('?')[:10]
  serializer = MovieListSerializer(movies, many=True)
  return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_form(request, user_pk):
  serializer = UserChoiceSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    serializer.save(user=request.user)

    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_userinfo(request):
    userchoice = get_object_or_404(UserChoice, user_id=request.user.pk)
    serializer = UserChoiceListSerializer(userchoice)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def suggest1(request):
  serializer = UserChoiceListSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    age = serializer['age']
    if age.value >= 19:
      movies = Movie.objects.filter(Rating__contains='청소년').order_by('?')[:10]
      serializers = MovieListSerializer(movies, many=True)
    elif 15 <= age.value < 19:
      movies = Movie.objects.filter(Rating__contains='15').order_by('?')[:10]
      serializers = MovieListSerializer(movies, many=True)
    elif 12 <= age.value < 15:
      movies = Movie.objects.filter(Rating__contains='12').order_by('?')[:10]
      serializers = MovieListSerializer(movies, many=True)
    else:
      movies = Movie.objects.filter(Rating__contains='전체').order_by('?')[:10]
      serializers = MovieListSerializer(movies, many=True)
  return Response(serializers.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def suggest2(request):
  serializer = UserChoiceListSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    p_age = serializer['parent_F']
    m_age = serializer['parent_M']
    avg = (p_age.value + m_age.value) // 20 + 2
    print(avg)
    movies = Movie.objects.filter(Release_date__contains=avg).order_by('?')[:10]
    serializers = MovieListSerializer(movies, many=True)
    return Response(serializers.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def suggest3(request):
  serializer = UserChoiceListSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    movies = Movie.objects.none()
    if serializer['drama'].value:
      movies = movies.union(Movie.objects.filter(summary__contains='드라마'))
    if serializer['fear'].value:
      movies = movies.union(Movie.objects.filter(summary__contains='공포'))
    if serializer['melloh'].value:
      movies = movies.union(Movie.objects.filter(summary__contains='멜로'))
    if serializer['thriller'].value:
      movies = movies.union(Movie.objects.filter(summary__contains='스릴러'))
    if serializer['comedey'].value:
      movies = movies.union(Movie.objects.filter(summary__contains='코미디'))
    if serializer['animation'].value:
      movies = movies.union(Movie.objects.filter(summary__contains='애니메이션'))
    if serializer['suspense'].value:
      movies = movies.union(Movie.objects.filter(summary__contains='서스펜스'))
    if serializer['action'].value:
      movies = movies.union(Movie.objects.filter(summary__contains='액션'))
    if serializer['sf'].value:
      movies = movies.union(Movie.objects.filter(summary__contains='SF'))  
    movies = movies[:5]
    serializers = MovieListSerializer(movies, many=True)
    return Response(serializers.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def suggest4(request):
  serializer = UserChoiceListSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    nation = serializer['Favorite'].value
    movies = Movie.objects.filter(country__contains=nation).order_by('?')[:10]
    serializers = MovieListSerializer(movies, many=True)
    return Response(serializers.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_kids(request):
  serializer = UserChoiceListSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    movies = Movie.objects.filter(summary__contains="애니메이션").order_by('?')[:10]
    serializers = MovieListSerializer(movies, many=True)
    return Response(serializers.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def form_update(request, info_pk):
  userchoice = get_object_or_404(UserChoice, pk=info_pk)
  serializer = UserChoiceSerializer(userchoice, data=request.data)
  if serializer.is_valid(raise_exception=True):
    serializer.save()
    return Response(serializer.data)