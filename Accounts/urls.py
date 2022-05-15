from django.urls import path
from Accounts import views

app_name = "Accounts"

urlpatterns = [
    path('user/register/', views.user_registration, name='user-register'),
    path('company/register/', views.company_registration, name='company-register'),
    # path('profile/edit<int:id/'/views.user_edit_prfile,name='edit-profile'),
    path('login/', views.user_logIn, name='login'),
    path('logout/', views.user_logOut, name='logout'),
]
