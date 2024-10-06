import phonenumbers
import opencage
import folium
from location import number

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber,'en')
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))


from opencage.geocoder import OpenCageGeocode

key = "fb51ca3fdf39474093a664eb4f39094b"
number = input("Enter phone number with country code:")
geocoder = OpenCageGeocode(key)
query  = str(location)
results = geocoder.geocode(query)
#print(results)
lat = results[0]["geometry"]["lat"]
lng = results[0]["geometry"]["lat"]

print(lat,lng)

myMap = folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat,lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")

'''
import phonenumbers
from phonenumbers import geocoder
from test import number
import folium

key = "fb51ca3fdf39474093a664eb4f39094b"

number = input("Entet phone number with country code:")
check_number = phonenumbers.parse(number)
number_location - geocoder.description_for_number(check_number, "en")
print(number_location)


from phone_number import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)

query = str(number_location)
results = geocoder.geocode(query)

lat =results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

map_location = folium.Map(location = [lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=number_location).add_to(map_location)
map_location.save("mylocation.html")
'''