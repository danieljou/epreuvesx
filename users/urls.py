from django.urls import path
from . import views

urlpatterns = [
    path("users_login/", views.users_login, name="users_login"),
    path("users_logout/", views.users_logout, name="users_logout"),
    path("account_management/", views.account_management, name="account_management"),
    path("account_add_user/", views.account_add_user, name="account_add_user"),
    path("account_upadate_user/<account_id>", views.account_upadate_user, name="account_upadate_user"),
    path("account_delete_user/<account_id>", views.account_delete_user, name="account_delete_user"),
    path("profile_user/",views.profile_user, name = "profile_user")
]
