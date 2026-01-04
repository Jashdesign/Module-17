import requests
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def get_weather(request):
    city = request.query_params.get('city')

    if not city:
        return Response(
            {"error": "City parameter is required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    api_key = os.getenv("WEATHER_API_KEY")
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )

    response = requests.get(url)
    if response.status_code != 200:
        return Response(
            {"error": "Unable to fetch weather data"},
            status=response.status_code
        )

    data = response.json()

    weather_data = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["description"],
    }

    return Response(weather_data, status=status.HTTP_200_OK)

@api_view(['POST'])
def get_lat_long(request):
    address = request.data.get('address')

    if not address:
        return Response(
            {"error": "Address is required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    url = (
        "https://maps.googleapis.com/maps/api/geocode/json"
        f"?address={address}&key={api_key}"
    )

    response = requests.get(url)
    data = response.json()

    if data["status"] != "OK":
        return Response(
            {"error": "Unable to fetch location"},
            status=status.HTTP_400_BAD_REQUEST
        )

    location = data["results"][0]["geometry"]["location"]

    return Response({
        "address": address,
        "latitude": location["lat"],
        "longitude": location["lng"]
    })

@api_view(['GET'])
def get_country_info(request, country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"

    response = requests.get(url)

    if response.status_code != 200:
        return Response(
            {"error": "Country not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    data = response.json()[0]

    country_data = {
        "name": data["name"]["common"],
        "capital": data.get("capital", ["N/A"])[0],
        "region": data["region"],
        "population": data["population"],
        "flag": data["flags"]["png"],
    }

    return Response(country_data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_github_user(request, username):
    url = f"https://api.github.com/users/{username}"

    headers = {
        "Authorization": f"token {os.getenv('GITHUB_TOKEN')}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return Response(
            {"error": "GitHub user not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    data = response.json()

    return Response({
        "username": data["login"],
        "name": data.get("name"),
        "public_repos": data["public_repos"],
        "followers": data["followers"],
        "profile_url": data["html_url"],
    })

@api_view(['POST'])
def create_github_repo(request):
    repo_name = request.data.get("repo_name")

    if not repo_name:
        return Response(
            {"error": "repo_name is required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    url = "https://api.github.com/user/repos"

    headers = {
        "Authorization": f"token {os.getenv('GITHUB_TOKEN')}"
    }

    payload = {
        "name": repo_name,
        "private": False
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code not in [200, 201]:
        return Response(
            {"error": "Failed to create repository"},
            status=response.status_code
        )

    return Response({
        "message": "Repository created successfully",
        "repo_url": response.json()["html_url"]
    })
