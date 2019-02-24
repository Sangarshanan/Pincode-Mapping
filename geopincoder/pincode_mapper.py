"""
The Main Pincode
Mapper fucntion extrapolating
pincode from geocodes
"""
from geopincoder.helper import *


class geocode: 

    def __init__(self): 
    	pass
      
    def to_pincode(self,lat,lon):
    	"""
    	Returns Pincode 
    	given latlongs
    	
    	Args:
    	    lat (Double): Latitude
    	    lon (Double): Longitude
    	
    	Returns:
    	    Integer: Pincode 
    	"""
    	return pincode_from_latlon(lat,lon)







