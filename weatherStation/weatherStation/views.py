from django.shortcuts import render

from weatherData.models import Wind

def homepage(request):
	windSpeed = Wind.objects.get(stationID="scholz_farm")
	context = {'windSpeed': windSpeed}
	return render(request, 'weatherData/homepage.html', context )