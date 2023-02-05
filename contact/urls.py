from django.urls import path

from contact import views

urlpatterns = [
    path('register/', views.RegisterContact.as_view()),
    path('<int:pk>/', views.ContactDetails.as_view()),
    path('', views.ListContacts.as_view())
]
