from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("login/", login_user, name="login"),
    path("register/", register_user, name="register"),
    path("token-refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("send-otp/", send_otp, name="send_otp"),
    path("reset-password/", reset_password, name="reset_password"),
    path("logout/", logout_user, name="logout"),
    path("users/", get_users, name="get_users"),
    path("profile/", get_user_profile, name="get_user_profile"),
    path("profile-update/", update_user_profile, name="update_user_profile"),
]
