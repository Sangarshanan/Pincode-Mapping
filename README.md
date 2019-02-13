# Pincodicem The Pincode Mapper

Map LatLongs to a Pincode 

Cities available 

- Ahmedabad	
- Bangalore	
- Chennai	
- Hyderabad	
- Kolkata	
- Mumbai	


### Clone this repo and install the package  

```
git clone https://github.com/Sangarshanan/Pincode-Mapping.git

python setup.py install
```

Now open your python interpreter

```python
from pincodicem import pincode_mapper as pm

pm.Geocode.to_bangalore_pin(<latitude>,<longitude>)


```

Used packages 

- fiona
- pandas 
- geopandas
- shapely

Data : https://github.com/datameet/PincodeBoundary

TODO: Looking to add more cities and expand the scope of this package
