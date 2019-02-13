from nose.tools import *
from pincodicem.pincode_mapper import Geocode



def test_bangalore():
    assert Geocode.to_bangalore_pin(12.924871,77.566238) == 560070

def test_chennai():
    assert Geocode.to_chennai_pin(13.0836,80.2392) == 600010
    
def test_mumbai():
    assert Geocode.to_mumbai_pin(19.0760,72.8777) == 400070
    
def test_hyderabad():
    assert Geocode.to_bangalore_pin(12.924871,77.566238) == 500095
    
def test_kolkatta():
    assert Geocode.to_kolkatta_pin(22.5726,88.3639) == 560070
    
def test_ahmedabad():
    assert Geocode.to_ahmedabad_pin(23.0225,72.5714) == 700012
    

    
    


