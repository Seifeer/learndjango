from django.urls import path

from . import views

urlpatterns = [
    #ex: /core/
    path('',views.base,name='base'),
    #ex:/core/5/
    #path('<int:Question_id>/',views.detail,name='Detail'),
    #ex:/core/5/results/
    #path('<int:Question_id>/results/',views.results,name='Results'),
    #ex:/core/5/vote/
    #path('<int:Question_id>/vote/',views.vote,name='Vote'),
]