# http://open-notify.org/Open-Notify-API/ISS-Location-Now/

import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib


def coord():
    req = urllib.Request("http://api.open-notify.org/iss-now.json")
    response = urllib.urlopen(req)
    data = response.read()

    obj = json.loads(data.decode("utf-8"))

    latitude, longitude = (obj['iss_position']['latitude'],
                           obj['iss_position']['longitude'])

    return latitude, longitude
