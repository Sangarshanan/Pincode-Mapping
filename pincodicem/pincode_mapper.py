import fiona
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon


def getpincode(data,lat , long):
    lat = float(lat)
    long = float(long)
    p = Point(long,lat)
    empty ="NOT AVAILABLE !! MAYBE TRY A DIFFERENT CITY"
    for i in range(0,len(data)):
        if p.within(data['geometry'][i]) is True:
            pin = int(data['pin_code'][i])
    try:
        pin # does a exist in the current namespace
    except NameError:
        pin = empty # nope
    return pin


blore = 'https://raw.githubusercontent.com/datameet/PincodeBoundary/master/Bangalore/boundary.geojson'
chen = 'https://raw.githubusercontent.com/datameet/PincodeBoundary/master/Chennai/boundary.geojson'
mum = 'https://raw.githubusercontent.com/datameet/PincodeBoundary/master/Mumbai/boundary.geojson'
ahme = 'https://raw.githubusercontent.com/datameet/PincodeBoundary/master/Ahmedabad/boundary.geojson'
kol =  'https://raw.githubusercontent.com/datameet/PincodeBoundary/master/Kolkata/boundary.geojson'
hyder = 'https://raw.githubusercontent.com/datameet/PincodeBoundary/master/Hyderabad/boundary.geojson'



class Geocode: 
    def __init__(self, lat, long): 
        self.lat = lat 
        self.long = long 
      
    @classmethod
    def to_bangalore_pin(cls,lat,long):
       
        fiona_collection = fiona.collection(blore)
        gdf = gpd.GeoDataFrame.from_features([feature for feature in fiona_collection])
        # Get the order of the fields in the Fiona Collection; add geometry to the end
        columns = list(fiona_collection.meta["schema"]["properties"]) + ["geometry"]
        # Re-order columns in the correct order
        gdf = gdf[columns]
        
        return (getpincode(gdf,lat,long))
    
    @classmethod
    def to_chennai_pin(cls,lat,long): 
        
        fiona_collection = fiona.collection(chen)
        gdf = gpd.GeoDataFrame.from_features([feature for feature in fiona_collection])
        # Get the order of the fields in the Fiona Collection; add geometry to the end
        columns = list(fiona_collection.meta["schema"]["properties"]) + ["geometry"]
        # Re-order columns in the correct order
        gdf = gdf[columns]
        gdf['pin_code'] = gdf['pin']

        
        return (getpincode(gdf,lat,long))
    
    @classmethod
    def to_mumbai_pin(cls,lat,long): 
        
        fiona_collection = fiona.collection(blore)
        gdf = gpd.GeoDataFrame.from_features([feature for feature in fiona_collection])
        # Get the order of the fields in the Fiona Collection; add geometry to the end
        columns = list(fiona_collection.meta["schema"]["properties"]) + ["geometry"]
        # Re-order columns in the correct order
        gdf = gdf[columns]
        
        return (getpincode(gdf,lat,long))
    
    @classmethod
    def to_ahmedabad_pin(cls,lat,long): 
        
        fiona_collection = fiona.collection(ahme)
        gdf = gpd.GeoDataFrame.from_features([feature for feature in fiona_collection])
        # Get the order of the fields in the Fiona Collection; add geometry to the end
        columns = list(fiona_collection.meta["schema"]["properties"]) + ["geometry"]
        # Re-order columns in the correct order
        gdf = gdf[columns]
        
        return (getpincode(gdf,lat,long))
    
    @classmethod
    def to_hyderabad_pin(cls,lat,long): 
        
        fiona_collection = fiona.collection(hyder)
        gdf = gpd.GeoDataFrame.from_features([feature for feature in fiona_collection])
        # Get the order of the fields in the Fiona Collection; add geometry to the end
        columns = list(fiona_collection.meta["schema"]["properties"]) + ["geometry"]
        # Re-order columns in the correct order
        gdf = gdf[columns]
        
        return (getpincode(gdf,lat,long))
    
    @classmethod
    def to_kolkatta_pin(cls,lat,long): 
        
        fiona_collection = fiona.collection(kol)
        gdf = gpd.GeoDataFrame.from_features([feature for feature in fiona_collection])
        # Get the order of the fields in the Fiona Collection; add geometry to the end
        columns = list(fiona_collection.meta["schema"]["properties"]) + ["geometry"]
        # Re-order columns in the correct order
        gdf = gdf[columns]
        
        return (getpincode(gdf,lat,long))
