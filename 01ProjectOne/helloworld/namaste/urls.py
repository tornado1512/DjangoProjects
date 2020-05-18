from django.urls import path
from . import views
urlpatterns=[
    path('namaste/',views.homePageView,name='home')

]