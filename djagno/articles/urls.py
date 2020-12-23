from django.urls import path, include
from . import views


app_name = 'articles'

urlpatterns = [
    # Movie
    path('', views.movie),
    path('<int:movie_pk>/', views.movie_detail),

    # Article
    path('<int:movie_pk>/create/', views.article_create),
    path('<int:movie_pk>/list/', views.article_list),
    path('<int:movie_pk>/<int:article_pk>/', views.article),
    path('<int:movie_pk>/<int:article_pk>/delete/', views.article_delete),
    path('<int:movie_pk>/<int:article_pk>/update/', views.article_update),

    # Comment
    path('<int:movie_pk>/<int:article_pk>/create/', views.comment_create),
    path('<int:movie_pk>/<int:article_pk>/index/', views.comment_list),
    path('<int:movie_pk>/<int:article_pk>/<int:comment_pk>/delete/', views.comment_delete),
    path('<int:movie_pk>/<int:article_pk>/<int:comment_pk>/update/', views.comment_update),

    # heart, thumb
    path('<int:movie_pk>/heart/', views.movie_heart),
    path('<int:article_pk>/thumb/', views.article_thumb),

    # recommendation
    path('people/', views.people),
    path('heart/', views.heart),
    path('score/', views.score),
    path('now/', views.now),
    path('serach_cry/', views.cry),
    path('serach_melloh/', views.melloh),
    path('serach_thriller/', views.thriller),
    path('serach_angry/', views.angry),

    path('<int:user_pk>/form/', views.create_form),
    path('<int:info_pk>/form_update/', views.form_update),
    path('get_userinfo/', views.get_userinfo),
    path('suggest1/', views.suggest1),
    path('suggest2/', views.suggest2),
    path('suggest3/', views.suggest3),
    path('suggest4/', views.suggest4),
    path('gokids/', views.get_kids),

]
