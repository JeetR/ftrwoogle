from django.urls import path

from SearchApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:q>/',views.search_words),
    path('<str:q>/async',views.search_words_async),
]