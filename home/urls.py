from django.urls import path

from . import views

app_name = "home"

urlpatterns =[
    path('',views.Home.as_view(),name = 'home'), #endpoint
    path('questions/',views.QuestionListView.as_view(),name = 'questions'),
    path('question/update/<int:pk>/',views.QuestionUpdateView.as_view(),name = 'update'),
    path('question/create/',views.QuestionCreateView.as_view(),name = 'create'),
    path('question/delete/<int:pk>/',views.QuestionDeleteView.as_view(),name = 'delete'),

]