"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

# main 폴더 안의 views.py를 불러옴
from . import views 

urlpatterns = [
    # path('url주소/', views.'views.py 안에 있는 뷰 이름', name="url이름"),
    path('', views.home, name="home"),
    path('create/', views.create_board, name="create_board"),
    path('read/', views.read_board, name="read_board"),
    # <int:pk> 는 html 에서 보내준 pk 값을 넘겨 받는 공간
    path('detail/<int:pk>',views.read_detail, name="read_detail"),
]
