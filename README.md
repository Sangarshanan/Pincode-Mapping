# Geopincoder 

Map LatLongs to a Pincode 

Cities available 

- Ahmedabad	
- Bangalore	
- Chennai	
- Hyderabad	
- Kolkata	
- Mumbai	
- Delhi


### Clone this repo and install the package  

Do this

```
pip install git+https://github.com/Sangarshanan/Pincode-Mapping.git
```

Or this

```
git clone https://github.com/Sangarshanan/Pincode-Mapping.git

python setup.py install
```

Now open your python interpreter

```python
from geopincoder import pincode_mapper as pm

pincode = pm.geocode.to_pincode(28.7041, 77.1025)
```


Data : https://github.com/datameet/PincodeBoundary

TODO: 

- Looking to add more cities and expand the scope of this package 
- Improve data quality with Google maps API for KDtrees clustering


