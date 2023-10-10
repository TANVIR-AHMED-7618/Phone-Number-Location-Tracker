import phonenumbers
import opencage
import folium
from Mynumber import number

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, 'en')

print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)

print(carrier.name_for_number(service_pro, 'en'))

from opencage.geocoder import OpenCageGeocode

key = "93c5f23af10943a7b7652cf1041be76c"

geocoder = OpenCageGeocode(key)

query = str(location)

results = geocoder.geocode(query)

#print(results)

lat = results[0]['geometry']['lat']
lag = results[0]['geometry']['lng']

print(lat, lag)

mymap = folium.Map(location=[lat, lag], zoom_start=12)
folium.Marker([lat,lag], popup=location).add_to(mymap)

mymap.save("myphonelocation.html")