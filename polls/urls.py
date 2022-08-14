from django.urls import path

from . import views #importa todas as vistas

app_name = 'polls'  #adiciona um namespace a este app para diferenciar caso criemos um novo app dentro desse projeto

#versão sem generic views
'''urlpatterns = [
    path('', views.index, name='index'),  #isso vai chamar a funcão index, dentro de "views"
                                           #path use 2 required args: route and view. 2 optional: kwargs and name 

    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]'''

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
