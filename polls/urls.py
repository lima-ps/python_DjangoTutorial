from django.urls import path

from . import views #importa todas as vistas

urlpatterns = [
    path('', views.index, name='index'),  #isso vai chamar a funcão index, dentro de "views"
                                           #path use 2 required args: route and view. 2 optional: kwargs and name 

    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]


