from nose.tools import *
from pincodicem.pincode_mapper import Geocode



def test_bangalore():
    assert Geocode.to_bangalore_pin(12.924871,77.566238) == 560070


