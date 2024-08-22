import phonenumbers
from phonenumbers import geocoder 
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
from getNumber import number
import folium
Key = "ce2cc6bd856d43558f01262ab2344ce1"
check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number, "en")
print(number_location)

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

geocoder = OpenCageGeocode(Key)

querry = str(number_location)
results = geocoder.geocode(querry)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

map_location = folium.Map(location = [lat,lng], zoom_start=9)
folium.Marker([lat,lng], popup=number_location).add_to(map_location)
map_location.save('location')
print("The Location is saved as location.html")