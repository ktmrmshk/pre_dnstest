import unittest

from dns_check import is_ip, DnsTester
import dns.name
import dns.rdatatype
import dns.rrset
import copy

class TestDnsCheck(unittest.TestCase):
  def setUp(self):
    self.dt = DnsTester('zone_revised.txt', 'a12-65.akam.net.')

  def test_get_query_answer(self):
    name, rdtype, rdataset = self.dt.get_rdataset_from_zone('www', 'A')
    ret = self.dt.get_query_answer(name, rdtype)
    self.assertEqual( type(ret), dns.rrset.RRset )

  def test_query_check(self):
    name, rdtype, rdataset = self.dt.get_rdataset_from_zone('www', 'A')
    ret = self.dt.query_check(name, rdataset)
    print(ret)

  def test_get_rdata_from_zone1(self):
    ret = self.dt.get_rdataset_from_zone('www', 'A')
    self.assertEqual( ret[0].to_text(), 'www')
    self.assertEqual( dns.rdatatype.to_text( ret[1] ), 'A'  )
    self.assertIsNotNone(ret[2])

  def test_get_rdata_from_zone2(self):
    ret = self.dt.get_rdataset_from_zone('www123', 'NS')
    self.assertEqual( ret[0].to_text(), 'www123')
    self.assertEqual( dns.rdatatype.to_text( ret[1] ), 'NS'  )
    self.assertIsNone(ret[2])

  
  def test_is_ip1(self):
    self.assertTrue( is_ip('1.2.3.4') )
 
  def test_is_ip2(self):
    self.assertTrue( is_ip('fe80::980f:62ff:fe74:203') )

  def test_is_ip3(self):
    self.assertFalse( is_ip('myexample.com') )




if __name__ == '__main__':
  unittest.main()

