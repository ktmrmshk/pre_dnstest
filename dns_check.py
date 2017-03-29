
# -*- coding: utf-8 -*-


'''
Summary: core code for DNS tester

Example:

Todo:
  * class 
  * Logger
  * docstring
  * Unittest code
  
  * Supporting Record Type:
   - A
   - AAAA
   - SOA
   - NS
   - MX
   - CNAME
   - TXT
   - SRV
'''

__author__ = 'Masahiko Kitamura'
__email__ = 'ktmrmshk@gmail.com'
__version__ = '0.01'
__date__ = '2017/3/22'


import dns.resolver
import dns.zone
import dns.rdatatype
import dns.name
import dns.rdatatype
import sys


import dns.ipv4
import dns.ipv6
def is_ip(text):
  'General Function to check if text is IP string or hostname'
  try:
    dns.ipv4.inet_aton(text)
    return True
  except Exception:
    try:
      dns.ipv6.inet_aton(text)
      return True
    except Exception:
      return False

class DnsTester(object):
  '''
  main class
  '''
  def __init__(self, zonefile, authns, zonename=None):
    '''
    Constructor
    
    Args:
    - zonefile: Zone file name
    - authns: Name of authoritative name server the test querys' sent to
    - zonename: Zone name of this zonefile. This can be omitted 
                if the zone file includes zone definition like 
                '$ORIGIN myexample.com'
    '''
    self.zonefile = zonefile
    self.authns = authns
    self.zone = dns.zone.from_file(self.zonefile)

    self.zonename = None
    if len(self.zone.origin.labels) != 0:
      self.zonename = self.zone.origin.to_text()
    elif zonename is not None:
      self.zonename = zonename
    if self.zonename is None:
      raise Exception('zonename is not valid: {}'.format(self.zonename))

    self.init_resolver()

  def init_resolver(self):
    '''
    for setting up resolver to throw queries to checks
    '''
    self.resolver = dns.resolver.Resolver()
    authns_ip = ''
    if is_ip(self.authns):
      authns_ip = self.authns
    else:
      authns_ip = self.resolv_ns(self.authns)
    self.nameservers = [authns_ip]
    print('authns_ip={}'.format(authns_ip)) 

  def query_check(self, name, rdataset):
    '''
    checks if name server has the entries same as one rdatasets has
    '''
    origin = dns.name.Name( self.zonename.split('.') )

    qname = name.derelativize(origin)
    print('name={}, type={}'.format(qname.to_text(), dns.rdatatype.to_text(rdataset.rdtype)))
    ans = self.resolver.query(qname.to_text(), dns.rdatatype.to_text(rdataset.rdtype))
    



  def echo_zone(self):
    print('Zone: {}'.format(self.zone.origin))
    print('===============')
    for name, node in self.zone.nodes.items():
      for rdataset in node.rdatasets:
        for d in rdataset:
          print('Name={}, d={}'.format(name.derelativize(self.zone.origin), d))
  
  def resolv_ns(self, authns):
    '''
    Func to resolve the target authoritative name server's IP 
    
    TODO:
      - should be by raising exception
    '''
    ans = dns.resolver.query(authns, 'A')
    return ans.rrset.items[0].address
    



def Func123(id):
    '''
    example function

    args:
    - id: int: id for this function
    '''
    pass

def test_zone_from_file():
  dt = DnsTester('zone_revised.txt', 'a12-65.akam.net.')
  dt.echo_zone()
  z = dt.zone
  rdataset = z.nodes[ list(z.nodes)[5] ].rdatasets[0]
  dt.query_check( list(z.nodes)[5], rdataset)


if __name__ == '__main__':
  test_zone_from_file()
  

