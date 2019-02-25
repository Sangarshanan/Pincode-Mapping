"""
HELPER FUCNTIONS FOR ABSTRACTION 
"""

import pandas as pd
import os
from sklearn.externals import joblib
from shapely.geometry import Point, Polygon

"""
Pickle file conataining the pandas 
dataframe for easy loading 

"""
s = (os.getcwd())
k = os.path.dirname(os.path.realpath(__file__))
k = str(k)

blore = k + '/data/blore.pkl'
chen = k+ '/data/chennai.pkl'
mum = k+'/data/mumbai.pkl'
ahme = k+'/data/ahmedabad.pkl'
kol =  k+'/data/kolkatta.pkl'
hyder = k+'/data/hyderabad.pkl'
delhi_data = k+'/data/delhi.csv'




def getpincode(data,lat,lon):

    """Gets pincode from
    the polygons shapefiles
    
    Args:
        data (str): Pickle path
        lat (double): latitude
        lon (double): longitude
    
    Returns:
        Integer: Pincode
    """
    lat = float(lat)
    lon = float(lon)
    p = Point(lon,lat)
    empty ="DATA NOT AVAILABLE"
    for i in range(0,len(data)):
        if p.within(data['geometry'][i]) is True:
            pin = int(data['pin_code'][i])
    try:
        pin # does a exist in the current namespace
    except NameError:
        pin = empty # nope
    return pin




def pincode_for_city(data,lat,lon):

    #fiona_collection = fiona.collection(cityname)
    #gdf = gpd.GeoDataFrame.from_features([feature for feature in fiona_collection])
    #columns = list(fiona_collection.meta["schema"]["properties"])+["geometry"]
    gdf = pd.read_pickle(data)

    try:
        gdf['pin_code'] = gdf['pin']
    except:
        pass

    return (getpincode(gdf,lat,lon))


def pincode_from_latlon(lat,lon):

        """
        Abstracts cities by 
        defining their bbox

        """

        if (lat > 12.602815 and lon > 76.863098 and lat < 13.386948 and lon <78.252869):
            #return "blore"
            return s
            #return pincode_for_city(blore,lat,lon)

        elif (lat > 18.687879 and lon > 72.410889 and lat < 19.539084 and lon <73.536987):
            #return "mum"
            return pincode_for_city(mum,lat,lon)

        elif (lat > 12.785018 and lon > 79.810181 and lat < 13.437709 and lon <80.529785):
            #return "chen"
            return pincode_for_city(chen,lat,lon)

        elif (lat > 16.830832 and lon > 77.755737 and lat < 17.942155 and lon <79.249878):
            #return "Hyderabad"
            return pincode_for_city(hyder,lat,lon)

        elif (lat > 22.446572 and lon > 71.883545 and lat < 23.301901 and lon <73.300781):
            return pincode_for_city(ahme,lat,lon)

        elif (lat > 21.473518 and lon > 87.583008 and lat < 23.216107 and lon <89.115601):
            return pincode_for_city(kol,lat,lon)

        elif (lat > 28.357568 and lon > 76.788940 and lat < 28.945669 and lon <77.503052):

        	#### KDtree bases approach for Delhi Pincode mapping (No Polygon data :( )

            data1 = pd.read_csv(delhi_data)

            filename = k+'/data/delhitree.sav'
            tree = joblib.load(filename)
            latlongs = [lat, lon]
            result = tree.query(latlongs)
            pincode_delhi = int(data1.iloc[[result[1]]]['postalcode'])
            return pincode_delhi



