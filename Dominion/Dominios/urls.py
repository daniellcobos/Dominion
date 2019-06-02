from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
app_name='dominios'
urlpatterns = [
    path('userlist', views.UserList.as_view()),
    path('userdetail/<str:username>', views.UserDetail.as_view()),
    path('Dominioslist', views.DominiosList.as_view()),
    path('Dominiosdetail/<str:Direction>', views.DominiosDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('usernamelist', views.Usernamelist.as_view()),
    path('Dominioreadlist/<str:Direction>',views.DominioReadlist.as_view()),
    path('DominiosExpired',views.DominioExpiredlist.as_view()),
    path('getTime', views.GetTime)
]