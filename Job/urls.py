import imp
from django.urls import path
from Job import views

app_name="Job"


urlpatterns = [
    path('',views.home_view,name='home'),
]
