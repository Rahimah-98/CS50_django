from django.urls import path

from.import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('rahimah', views.rahimah, name='rahimah'),
    path("<str:name>", views.greet, name='greet'),
]
 