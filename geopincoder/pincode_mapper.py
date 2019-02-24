"""
The Main Pincode
Mapper fucntion extrapolating
pincode from geocodes
"""
from geopincoder.helper import *


class geocode: 

    def __init__(self): 
    	pass
    
    @staticmethod
    def to_pincode(lat,lon):
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







