from django.urls import path
from .views import QuestionsView, UserView, LeaderboardView

urlpatterns = [
    path('getquestions/', QuestionsView.as_view(), name = 'getquestions'),
    path('getoneuser/', UserView.as_view(), name='getoneuser'),
    path('getallusers/', UserView.as_view(), name='getallusers'),
    path('register/', UserView.as_view(), name='register'),
    path('login/', UserView.as_view(), name='login'),
    path('logout/', UserView.as_view(), name='logout'),
    path('add_points/', LeaderboardView.as_view(), name='add_points'),
    path('update_points/', LeaderboardView.as_view(), name='update_points'),
    path('leaderboard/', LeaderboardView.as_view(), name='leaderboard'),
]