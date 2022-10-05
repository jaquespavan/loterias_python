#http://www.geoplugin.net/json.gp?ip=xx.xx.xx.xx
import requests
import json
#import pprint

accuweatherapikey = '1Ato8qgHddau4tJKJ4WSBWIeClXC2saf'

def pegarCoordenadas():

    r = requests.get('http://www.geoplugin.net/json.gp')

    if (r.status_code != 200):
        print(r.status_code)
        print('Não foi possível obter a localização')
        return None 
    else:
        try:
            #print(type(json.loads(r.text)))
            localizacao = json.loads(r.text)
            coordenadas = {}
            coordenadas['lat'] = localizacao['geoplugin_latitude']
            coordenadas['long'] = localizacao['geoplugin_longitude']
            #print(pprint.pprint(localizacao))
            #print('Latitude:', lat)
            #print('Longitude:', long)
            return coordenadas
        except:
            return None

#http://dataservice.accuweather.com/currentconditions/v1/#codigolocal
#http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=1Ato8qgHddau4tJKJ4WSBWIeClXC2saf&q=-21.8265%2C-48.2023&language=pt-br
#http://dataservice.accuweather.com/currentconditions/v1/36343?apikey=1Ato8qgHddau4tJKJ4WSBWIeClXC2saf&language=pt-br    

def pegarCodigoLocal(lat, long):

    locationapiurl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=" + accuweatherapikey + "&q=" + lat + "%2C" + long + "&language=pt-br"
    r = requests.get(locationapiurl)
    if (r.status_code != 200):
        print(r.status_code)
        print('Não foi possível obter o codigo do local')
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

## inicio do programa

try:

    coordenadas = pegarCoordenadas()
    local = pegarCodigoLocal(coordenadas['lat'], coordenadas['long'])

    #print(coordenadas)
    #print(local)

    climaAtual = pegarTempoAgora(local['codigolocal'], local['nomelocal'])
    print('▄▀▄ PREVISÃO DO TEMPO ▄▀▄' + '\n')
    print('CIDADE: ' + climaAtual['nomeLocal'] + '.')
    print('CLIMA: ' + climaAtual['textoclima'])
    print('Temperatura: ' + str(climaAtual['temperatura']) + '\xb0' + 'C' + '\n')

    print('PREVISÃO PARA OS PRÓXIMOS 5 DIAS:' + '\n')
    print('▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀' + '\n')

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
            print('▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀' + '\n')
    
except:
    print('Não foi possível obter os dados')

'''
    #print(coordenadas)
    #print(local)
    #print(climaAtual)


#    coordenadas = pegarCoordenadas()
#    local = pegarCodigoLocal(coordenadas['lat'], coordenadas['long'])

    #print(coordenadas)
    #print(local)

    #print(str(local['codigolocal']))
    #print(str(accuweatherapikey))

    #http://dataservice.accuweather.com/forecasts/v1/daily/5day/36343?apikey=1Ato8qgHddau4tJKJ4WSBWIeClXC2saf&language=pt-br&details=true&metric=true
'''

