

import geocoder
g = geocoder.ip('me')
print(g)

# import googlemaps
# gmaps = googlemaps.Client(key='my_key')



def get_location_by_ip(ip='me'):
    return geocoder.ip(ip)

# def get_location_accurate():
#     loc = gmaps.geolocate()
#     print(loc)