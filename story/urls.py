
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('books/', views.books, name = "books"),
    path('upload/', views.upload, name='upload'),
    path('audio/', views.audio, name='audio'),
    path('read/<int:id>', views.read, name='read'),

    path('record/', views.record, name='record'),
    path('audioplay/<int:id>', views.audioplay, name='audioplay'),
    path('postComment/', views.postComment, name='postComment')
]
