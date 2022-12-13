from django.urls import path
from . import views
urlpatterns = [
    path('blog/',views.HomePage.as_view() , name ='multiplepost'),
    path('blog/<slug:slug>/',views.PostDetail.as_view(), name="postPage"),
    #path('category/<str:str>/',views.Category.as_view(),name ="category"),
    path('category/<int:pk>/',views.category,name ="category"),
    path('1/<int:pk>/',views.Category.as_view(),name ="category1"),
    #path('sw.js',views.blog ),
]