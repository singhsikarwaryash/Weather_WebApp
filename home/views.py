from django.shortcuts import render
#from matplotlib.style import context
import requests
import datetime
from datetime import datetime
import calendar
# Create your views here.
def home(request):
    current_date = datetime.now()
    current_day = datetime.today().strftime('%A')
    #today = datetime.now().day
    city = request.GET.get('city' , "Lucknow")
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=b6fbf9ea453ed19b776405d908e0eab0'
    data = requests.get(url).json()
    payload = {
        'date' : current_date,
        'day' : current_day,
        'city' : data['name'],
        'weather' : data['weather'][0]['main'],
        'icon' : data['weather'][0]['icon'],
        'fahrenhiet_temperature' : int(((data['main']['temp'] -273)*9/5)+32),
        'calcius_temperature' : int(data['main']['temp'] - 273),
        'pressure' : data['main']['pressure'],
        'humidity' : data['main']['humidity'],
        'description' : data['weather'][0]['description']
    }
    context = {'data' : payload}
    print(context)
   
    return render(request, 'home.html' ,  context )