import geopandas as gpd
import pandas as pd
from shapely.geometry import Point, Polygon


def getpincode(data, lat, long):
    lat = float(lat)
    long = float(long)
    p = Point(long, lat)
    empty = "NOT AVAILABLE !! MAYBE TRY A DIFFERENT CITY"
    for i in range(0, len(data)):
        if p.within(data['geometry'][i]) is True:
            pin = int(data['pin_code'][i])
    try:
        pin
    except NameError:
        pin = empty
    return pin


class Geocode:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

    @classmethod
    def to_bangalore_pin(cls, lat, long):
        data = gpd.read_file('data/blore.geojson')
        return getpincode(data, lat, long)

    @classmethod
    def to_chennai_pin(cls, lat, long):
        data = gpd.read_file('data/chennai.geojson')
        data['pin_code'] = data['pin']
        return getpincode(data, lat, long)

    @classmethod
    def to_mumbai_pin(cls, lat, long):
        data = gpd.read_file('data/mumbai.geojson')
        return getpincode(data, lat, long)

    @classmethod
    def to_ahmedabad_pin(cls, lat, long):
        data = gpd.read_file('data/ahmedabad.geojson')
        return getpincode(data, lat, long)

    @classmethod
    def to_hyderabad_pin(cls, lat, long):
        data = gpd.read_file('data/hyderabad.geojson')
        return getpincode(data, lat, long)

    @classmethod
    def to_kolkatta_pin(cls, lat, long):
        data = gpd.read_file('data/kolkatta.geojson')
        return getpincode(data, lat, long)