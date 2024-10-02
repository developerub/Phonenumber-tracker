import phonenumbers
from phonenumbers import geocoder 
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
from getNumber import number
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
print(lat,lng)
print("....Search the above values on google map to get that location....")
