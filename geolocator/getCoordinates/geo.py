from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='geolocator')

def getCoordinates(spot):
    try:
        location = geolocator.geocode(spot)
        return spot, location.latitude, location.longitude
    except:
        return 'Spot not found!'
   