from collections import namedtuple
from geopy.geocoders import Nominatim, GoogleV3

country_info = namedtuple('country_info',
                          'name country_code')


def info(coordinates):
    '''
    Input
        coordinates should be a tuple which contains (latitude, longitude)
    Output
        named tuple with the following fields: name country country_code state
    '''
    for geocoder in [Nominatim(country_bias='PH'), GoogleV3()]:
        geolocator = geocoder
        location = geolocator.reverse("{}, {}".format(*coordinates))

        if (location is not None and
           location.address is not None):
            return country_info(location['address'],
                                location.raw['address']['country_code'])

    # default
    return country_info(None, 'US')
