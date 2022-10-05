# pk.eyJ1IjoiamFxdWVzcGF2YW4iLCJhIjoiY2tnMmxudzlsMDF6aDMwcDZ0ZHNlaWxhZCJ9.ulEmpeU6m644i2fIz6WYRg

import requests
import json
import pprint

mapboxapikey = 'pk.eyJ1IjoiamFxdWVzcGF2YW4iLCJhIjoiY2tnMmxudzlsMDF6aDMwcDZ0ZHNlaWxhZCJ9.ulEmpeU6m644i2fIz6WYRg'

cidade = input('Cidade: ')
estado = input('Estado: ')
#país = input('País: ')

url = 'https://api.mapbox.com/geocoding/v5/mapbox.places/' + cidade + '.json?types=place&access_token=pk.eyJ1IjoiamFxdWVzcGF2YW4iLCJhIjoiY2tnMmxudzlsMDF6aDMwcDZ0ZHNlaWxhZCJ9.ulEmpeU6m644i2fIz6WYRg'

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
	print('Local: ' + local)
	print('Latitude: ' + str(lati))
	print('Longitude: ' + str(longi))
		
'''
	localizacao = conteudo.get('features')
	print(type(localizacao))
	print(localizacao)
'''    

'''
    localizacao = json.loads(r.text)
    lat = localizacao['geoplugin_latitude']
    long = localizacao['geoplugin_longitude']
    #print(pprint.pprint(localizacao))
    print('Latitude:', lat)
    print('Longitude:', long)
'''