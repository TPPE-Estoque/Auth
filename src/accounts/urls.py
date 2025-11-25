from django.urls import path
from .views import RegisterView, UserDetailView


app_name = 'accounts'

urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
