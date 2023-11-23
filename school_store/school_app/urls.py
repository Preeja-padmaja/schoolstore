from. import views
from django .urls import path
urlpatterns = [
    path('', views.school_fun,name='school_fun'),
    path('login/',views.login_fun,name='login_fun'),
    path('register/',views.register_fun,name='register_fun'),
    path('logout/',views.logout_fun,name='logout_fun'),
    path('user_page/',views.user_fun,name='user_fun'),
]