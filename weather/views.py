import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CityForm()

    all_cities_info = get_all_cities_info()
    context = {'all_cities_info': all_cities_info, 'form': form}

    return render(request, 'weather/index.html', context)


def remove_city(request):
    if request.method == 'POST':
        city = City.objects.get(id=int(request.POST.get('city_id')))
        city.delete()

        form = CityForm()
        all_cities_info = get_all_cities_info()
        context = {'all_cities_info': all_cities_info, 'form': form}
        return render(request, 'weather/index.html', context)


def get_all_cities_info():
    appid = '2c8c85f9581714ced1d35140700605e1'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    cities = City.objects.all()
    all_cities_info = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        print(res)
        city_info = {
            'city': city.name,
            'id': city.id,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
        }
        all_cities_info.append(city_info)
    return all_cities_info
