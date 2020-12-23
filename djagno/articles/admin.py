from django.contrib import admin
from .models import Article, Comment, Movie


admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Movie)
