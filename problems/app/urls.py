from django.urls import path
from app.views import views,RecentPostsView

urlpatterns = [
    path('initial/', views.app, name='app'), # http://127.0.0.1:8000/app/initial/
    path('recent_posts/', RecentPostsView.as_view(), name='recent_posts'),

] 