#http://www.geoplugin.net/json.gp?ip=xx.xx.xx.xx
import requests
import json
import pprint

accuweatherapikey = '1Ato8qgHddau4tJKJ4WSBWIeClXC2saf'

r = requests.get('http://www.geoplugin.net/json.gp')

if (r.status_code != 200):
    print('Não foi possível obter a localização')
else:
    #print(type(json.loads(r.text)))
    localizacao = json.loads(r.text)
    lat = localizacao['geoplugin_latitude']
    long = localizacao['geoplugin_longitude']
    #print(pprint.pprint(localizacao))
    print('Latitude:', lat)
    print('Longitude:', long)

#http://dataservice.accuweather.com/currentconditions/v1/#codigolocal
#http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=1Ato8qgHddau4tJKJ4WSBWIeClXC2saf&q=-21.8265%2C-48.2023&language=pt-br
#http://dataservice.accuweather.com/currentconditions/v1/36343?apikey=1Ato8qgHddau4tJKJ4WSBWIeClXC2saf&language=pt-br    

    locationapiurl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=" + accuweatherapikey + "&q=" + lat + "%2C" + long + "&language=pt-br"
    r2 = requests.get(locationapiurl)
    if (r.status_code != 200):
        print('Não foi possível obter o codigo do local')
    else:
        locationresponse = json.loads(r2.text)
        #print(locationresponse)
        nomelocal = locationresponse['LocalizedName'] + '-' + locationresponse['AdministrativeArea']['LocalizedName'] + '. ' + locationresponse['Country']['LocalizedName']
        codigolocal = locationresponse['Key']
        print('Local:', nomelocal)
        #print('Cod local:', codigolocal)

        currentconditionsapiurl = "http://dataservice.accuweather.com/currentconditions/v1/" + codigolocal + "?apikey=" + accuweatherapikey + "&language=pt-br"
        r3 = requests.get(currentconditionsapiurl)
        if (r.status_code != 200):
            print('Não foi possível obter a condição do tempo')
        else:
            currentconditionsresponse = json.loads(r3.text)
            #print(pprint.pprint(currentconditionsresponse))
            textoclima = currentconditionsresponse[0]['WeatherText']
            temperatura = currentconditionsresponse[0]['Temperature']['Metric']['Value']
            print('Clima:', textoclima)
            print('Temperatura: ' + str(temperatura) + 'º C')
            
         
    
    
    



