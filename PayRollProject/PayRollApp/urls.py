from django.urls import path

from PayRollApp import views


urlpatterns=[
    path('',views.emp_view),
]