from collections import namedtuple
from geopy.geocoders import Nominatim


def info(coordinates):
    '''
    Input
        coordinates should be a tuple which contains (latitude, longitude)
    Output
        named tuple with the following fields: name country country_code state
    '''
    geolocator = Nominatim()

    location = geolocator.reverse("{}, {}".format(*coordinates))
    country_info = namedtuple('country_info',
                              'name country_code')
    return country_info(location['address'],
                        location.raw['address']['country_code'])
