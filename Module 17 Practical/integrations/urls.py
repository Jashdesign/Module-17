from django.urls import path
from .views import get_weather,get_lat_long,get_country_info,create_github_repo,get_github_user

urlpatterns = [
    path('weather/', get_weather, name='weather'),
    path('geocode/',get_lat_long,name='geocode'),
    path('country/<str:country_name>/', get_country_info,name='country_info'),
    path('github/user/<str:username>/', get_github_user,name='get_github'),
    path('github/create-repo/', create_github_repo,name='create_github'),
]