from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('login/',views.user_login,name='user_lgoin'),
    #path('<int:article_id>/',views.blog_article,name='blog_article'),
    ]
