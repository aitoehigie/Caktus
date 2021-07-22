from django.urls import path
from . import views

urlpatterns = [
    path('drill/', views.drill, name='xword-drill'),
    path('answer/<str:clue_id>', views.answer,  name='xword-answer'),
]