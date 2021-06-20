from django.urls import path
from . import views

app_name = 'blog'

urlpatterns =[
    path('', views.IndexView.as_view(), name='index'),
    path('blog-detail/<int:pk>/',views.BlogDetail.as_view(), name='blog_detail'),
    path('science-list',views.ScienceView.as_view(), name='science_list'),
    path('dailylife-list',views.DailyLifeView.as_view(), name= 'daylylife_list'),
    path('music-list',views.MusicView.as_view(), name='music_list'),
    path('contact/',views.ContactView.as_view(), name='contact')
]
