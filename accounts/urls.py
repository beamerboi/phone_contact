from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.BlacklistRefreshView.as_view(), name="logout"),
    path('me/update/', views.ProfileUpdateAPIView.as_view()),
    path('me/', views.ProfileDetailAPIView.as_view()),
    path('<int:pk>/', views.UserProfileDetail.as_view()),
]