import unittest

from dns_check import is_ip, DnsTester
import dns.name
import dns.rdatatype
import dns.rrset
import copy

zonetxt='''$ORIGIN myexample.com
$TTL		3600
@       			IN	SOA     a12-65.akam.net. hostmaster.akamai.com. (
				2016111701
				10800
				3600
				604800
				86400 )
;
							IN	NS			a12-65.akam.net.
							IN	NS			a4-65.akam.net.
							IN	NS			a13-65.akam.net.
							IN	NS			a9-67.akam.net.
							IN	NS			a1-76.akam.net.
							IN	NS			a20-65.akam.net.

www			1800	IN	A       10.20.30.40
        1800	IN	A       10.20.30.50
        1800	IN	A       10.20.30.60

www2				  IN	A       10.20.30.41
util    			IN	A			 	10.20.30.42
file    			IN	CNAME   util    
backup  			IN	CNAME		util


mail    			IN	MX  		0 10.20.30.43
        			IN	MX  		20 10.20.30.45
        			IN	MX  		10 10.20.30.46
							IN	TXT			"v=spf1 +ip4:192.168.100.0/24 +ip4:10.0.0.0/24 ~all"




'''



class TestDnsCheck(unittest.TestCase):
  def setUp(self):
    self.dt = DnsTester('a12-65.akam.net.')
    self.dt.load_file('zone_revised.txt')
 
  def test_load_txt(self):
    dt1 = DnsTester('a12-65.akam.net.')
    dt1.load_txt(zonetxt)

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

  def test_zone_check(self):
    ret = self.dt.zone_check()
    print(ret)
  
  def test_is_ip1(self):
    self.assertTrue( is_ip('1.2.3.4') )
 
  def test_is_ip2(self):
    self.assertTrue( is_ip('fe80::980f:62ff:fe74:203') )

  def test_is_ip3(self):
    self.assertFalse( is_ip('myexample.com') )




if __name__ == '__main__':
  unittest.main()

