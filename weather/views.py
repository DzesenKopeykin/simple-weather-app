import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    appid = '2c8c85f9581714ced1d35140700605e1'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities_info = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        print(url.format(city.name))
        print(res)
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
        }
        all_cities_info.append(city_info)

    print(all_cities_info)
    context = {'all_cities_info': all_cities_info, 'form': form}

    return render(request, 'weather/index.html', context)
