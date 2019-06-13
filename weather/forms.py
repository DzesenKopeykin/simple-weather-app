import requests
from .models import City
from django.forms import ModelForm, TextInput


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={
            'class': 'form-control',
            'name': 'city',
            'id': 'city',
            'placeholder': 'Введите город'
        })}

    def is_valid(self):
        valid = super(CityForm, self).is_valid()

        appid = '2c8c85f9581714ced1d35140700605e1'
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
        res = requests.get(url.format(self.data['name'])).json()
        print(res)
        if valid and res['cod'] == 200:
            return True
        else:
            return False
