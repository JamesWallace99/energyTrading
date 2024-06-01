import numpy as np
from solarpy import solar_panel
from solarpy import irradiance_on_plane
import datetime

# opencage API call forward geocodes a city location from DESNZ report
# solarpy simulates power output for solar panels with a defined size and location 
# assumes clear sky irradiance - doesn't account for weather


# forward geocoding for lat and long
panel_area = 2
panel_efficiency = 0.2
query = u"Oxford, England, UK"
print(f"Getting Solar panel output for {panel_area}m^2 panel in {query}.")

from opencage.geocoder import OpenCageGeocode

key = '87ada2f6b3d645458229d8fae2c45aa8'
geocoder = OpenCageGeocode(key)

# no need to URI encode query, module does that for you
results = geocoder.geocode(query)

print(u'%f;%f;%s;%s' % (results[0]['geometry']['lat'],
                        results[0]['geometry']['lng'],
                        results[0]['components']['country_code'],
                        results[0]['annotations']['timezone']['name']))

lat = results[0]['geometry']['lat']
long = results[0]['geometry']['lng']

panel = solar_panel(2, 0.2, id_name='NYC_xmas')  # surface area m^2, efficiency and name
panel.set_orientation(np.array([0, 0, -1]))  # upwards
panel.set_position(lat, long, 0)  # NYC latitude, longitude, altitude
panel.set_datetime(datetime.datetime(2019, 10, 17, 13, 1))  # Christmas Day!
panel.power() # in W


vnorm = np.array([0, 0, -1])  # plane pointing zenith
h = 0  # sea-level
date = datetime.datetime(2019, 10, 17, 13, 1)  # year, month, day, hour, minute
print("solarpy irradiance estimate (W / m^2): ", irradiance_on_plane(vnorm, h, date, lat))
print("solarpy panel output (W): ", panel.power())