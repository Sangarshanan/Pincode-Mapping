from geopincoder.helper import *


class geocode: 
    def __init__(self, lat, lon): 
        self.lat = lat 
        self.lon = lon



      
    @classmethod
    def to_pincode(cls,lat,lon):

    	return pincode_from_latlon(lat,lon)







