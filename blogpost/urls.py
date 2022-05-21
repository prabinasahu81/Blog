"""drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# from blogpost import views
from blogpost.views import HomeView,ArticleDetail,AddPostView,UpdatePostView,DeletePostView
# from blogpost.views import ArticleDetail,AddPostView
urlpatterns = [
    # path('', views.home,name="home"),
    path('', HomeView.as_view(),name="home"),
    path('article/<int:pk>', ArticleDetail.as_view(),name="article_detail"),
    path('add_post/', AddPostView.as_view(),name="add_post"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(),name="update_post"),
    path('article/<int:pk>/delete', DeletePostView.as_view(),name="delete_post"),

]
