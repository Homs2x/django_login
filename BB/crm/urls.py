from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.homepage, name=""),

    path('register', views.register, name="register"),

    path('my-login', views.my_login, name="my-login"),

    path('dashboard', views.dashboard, name="dashboard"),

    path('user-logout', views.user_logout, name="user-logout"),

    path('orglist', views.orglist, name="orglist"),

    path('locate', views.locate, name="locate"),

    path('feedback', views.feedback, name="feedback"),

    path('account', views.account, name="account"),

    path('donate', views.donate, name="donate"),
]










