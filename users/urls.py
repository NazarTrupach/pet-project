from django.urls import path
from django.contrib.auth.decorators import login_required
from users.views import login, UserRegistrationView, UserProfileView, logout, EmailVerificationView

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),
    path('logout/', logout, name='logout'),
    path('verify/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='email_verification'),
]