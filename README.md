# Pincodicem

Map LatLongs to a Pincode 

Cities available 

- Ahmedabad	
- Bangalore	
- Chennai	
- Hyderabad	
- Kolkata	
- Mumbai	


### To use this package follow the instructions 

```
git clone https://github.com/Sangarshanan/Pincode-Mapping.git

python setup.py install
```

Now open your python interpreter

```python
from pincodicem import pincode_mapper as pm

pm.Geocode.to_bangalore_pin(<latitude>,<longitude>)


```

Data : https://github.com/datameet/PincodeBoundary
