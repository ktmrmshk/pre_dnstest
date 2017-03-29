import unittest

from dns_check import is_ip, DnsTester
import dns.name


class TestDnsCheck(unittest.TestCase):
  def setUp(self):
    self.dt = DnsTester('zone_revised.txt', 'a12-65.akam.net.')
    

  #def test_query_check(self):
  #  name = dns.name.Name('www')
  #  dt.query_check(name, None)
    

  
  def test_is_ip1(self):
    self.assertTrue( is_ip('1.2.3.4') )
 
  def test_is_ip2(self):
    self.assertTrue( is_ip('fe80::980f:62ff:fe74:203') )

  def test_is_ip3(self):
    self.assertFalse( is_ip('myexample.com') )




if __name__ == '__main__':
  unittest.main()

