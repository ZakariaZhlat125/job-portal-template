import imp
from django.urls import path
from Job import views

app_name="Job"


urlpatterns = [
    path('',views.home_view,name='home'),
    path('jobs/',views.create_job_view,name="create-job"),
    path('job/create/',views.single_job_view,name='single-job')

]
