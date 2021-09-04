from django.urls import path
from .import views
urlpatterns = [
    path('',views.chat,name="index"),
    path('get',views.get,name="try"),
    path("signup/",views.signup,name='signup'),
    path('login/',views.Login,name="login"),
    path("logout/",views.Logout)
]