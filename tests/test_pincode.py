import unittest
from geopincoder import mapper



class TestCityPincodes(unittest.TestCase):


    def test_bangalore(self):

        self.assertEqual(mapper.to_pincode(12.924871,77.566238),560070)

    def test_mumbai(self):

        self.assertEqual(mapper.to_pincode(19.0896 , 72.8656),400099)

    def test_chennai(self):

        self.assertEqual(mapper.to_pincode(13.1090, 80.2049),600049)

    def test_hyderabad(self):

        self.assertEqual(mapper.to_pincode(17.3616, 78.4747),500002)

    def test_delhi(self):

        self.assertEqual(mapper.to_pincode(28.7041, 77.1025),110083)

    def test_kolkatta(self):

        self.assertEqual(mapper.to_pincode(22.5726, 88.3639),700012)

    def test_ahmedabad(self):

        self.assertEqual(mapper.to_pincode(23.0225, 72.5714),380006)




#print(mapper.to_pincode(12.924871,77.566238))

#print(mapper.to_pincode(19.0896 , 72.8656))

#print(mapper.to_pincode(13.1090, 80.2049))

#print(mapper.to_pincode(17.3616, 78.4747))

#print(mapper.to_pincode(28.7041, 77.1025))


    


