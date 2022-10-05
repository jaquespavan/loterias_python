import requests
import json
#import pprint

#PRECISA MELHORAR A DATA

mapboxapikey = 'pk.eyJ1IjoiamFxdWVzcGF2YW4iLCJhIjoiY2tnMmxudzlsMDF6aDMwcDZ0ZHNlaWxhZCJ9.ulEmpeU6m644i2fIz6WYRg'
accuweatherapikey = '1Ato8qgHddau4tJKJ4WSBWIeClXC2saf'

cidade = input('DIGITE A CIDADE: ')
estado = input('DIGITE O ESTADO: ')
#país = input('País: ')

def coordenadasInput(cidade):

	url = 'https://api.mapbox.com/geocoding/v5/mapbox.places/' + cidade + ',' + estado + '.json?types=place&access_token=pk.eyJ1IjoiamFxdWVzcGF2YW4iLCJhIjoiY2tnMmxudzlsMDF6aDMwcDZ0ZHNlaWxhZCJ9.ulEmpeU6m644i2fIz6WYRg'

	r = requests.get(url)

	if (r.status_code != 200):
	    print(r.status_code)
	    print('Não foi possível obter os dados')
	else:
		#print(r.status_code)
		conteudo = json.loads(r.text)
		#print(type(conteudo))
		#print(conteudo)
		local = conteudo['features'][0]['place_name']
		longi = conteudo['features'][0]['geometry']['coordinates'][0]
		lati = conteudo['features'][0]['geometry']['coordinates'][1]
		
		return(local, lati, longi)

def pegarCodigoLocal(lati, longi):

    locationapiurl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=" + accuweatherapikey + "&q=" + str(lati) + "%2C" + str(longi) + "&language=pt-br"
    r = requests.get(locationapiurl)
    if (r.status_code != 200):
        print(r.status_code)
        print('Não foi possível obter o código do local')
        return None
    else:
        try:
            locationresponse = json.loads(r.text)
            infoLocal = {}
            #print(locationresponse)
            infoLocal['nomelocal'] = locationresponse['LocalizedName'] + '-' + locationresponse['AdministrativeArea']['LocalizedName'] + '. ' + locationresponse['Country']['LocalizedName']
            infoLocal['codigolocal'] = locationresponse['Key']
            #print('Local:', nomelocal)
            #print('Cod local:', codigolocal)
            return infoLocal
        except:
            return None

def pegarTempoAgora(codigolocal, nomelocal):

    currentconditionsapiurl = "http://dataservice.accuweather.com/currentconditions/v1/" + codigolocal + "?apikey=" + accuweatherapikey + "&language=pt-br"
    
    r = requests.get(currentconditionsapiurl)
    if (r.status_code != 200):
        print(r.status_code)
        print('Não foi possível obter a condição do tempo')
        return None
    else:
        try:
            currentconditionsresponse = json.loads(r.text)
            infoClima = {}
            #print(pprint.pprint(currentconditionsresponse))
            infoClima['textoclima'] = currentconditionsresponse[0]['WeatherText']
            infoClima['temperatura'] = currentconditionsresponse[0]['Temperature']['Metric']['Value']
            infoClima['nomeLocal'] = nomelocal
            #print('Clima:', textoclima)
            #print('Temperatura: ' + str(temperatura) + 'º C')
            return infoClima
        except:
            return None


coord = coordenadasInput(cidade)
#print(coord)

#print('Local: ' + coord[0])
#print('Latitude: ' + str(coord[1]))
#print('Longitude: ' + str(coord[2]))


local = pegarCodigoLocal(coord[1], coord[2])
#print(local)

climaAtual = pegarTempoAgora(local['codigolocal'], local['nomelocal'])

print('\n▄▀▄ PREVISÃO DO TEMPO ▄▀▄' + '\n')
print('LOCAL: ' + climaAtual['nomeLocal'] + '.')
print('CIDADE: ' + str(coord[0]))
print('LATITUDE: ' + str(coord[1]))
print('LONGITUDE: ' + str(coord[2]))
print('CLIMA: ' + climaAtual['textoclima'])
print('Temperatura: ' + str(climaAtual['temperatura']) + '\xb0' + 'C' + '\n')

print('PREVISÃO PARA OS PRÓXIMOS 5 DIAS:' + '\n')
print('▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄' + '\n')

#proximos 5 dias

fiveDaysUrl = 'http://dataservice.accuweather.com/forecasts/v1/daily/5day/' + str(local['codigolocal']) + '?apikey=' + str(accuweatherapikey) + '&language=pt-br&details=true&metric=true'

r = requests.get(fiveDaysUrl)

if (r.status_code != 200):
	print('Não foi possível obter a condição do tempo dos próximos 5 dias.')
    #return None
else:
	fiveDaysResponse = json.loads(r.text)
	#print(type(fiveDaysResponse))
	for i in range(5):
		data = fiveDaysResponse['DailyForecasts'][i]['Date']
		tempMin = fiveDaysResponse['DailyForecasts'][i]['Temperature']['Minimum']['Value']
		tempMax = fiveDaysResponse['DailyForecasts'][i]['Temperature']['Maximum']['Value']
		textoclima = fiveDaysResponse['DailyForecasts'][i]['Day']['IconPhrase']
		print('Data:', data)
		print('Temperatura Mínima:', tempMin)
		print('Temperatura Máxima:', tempMax)
		print('Clima:', textoclima, '\n')
		print('▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄' + '\n')
