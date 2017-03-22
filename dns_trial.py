import dns.resolver
import dns.zone
import dns.rdatatype 
import sys

def fqdn(name, origin):
	if name.labels==():
		return '%s' % origin
	return '%s.%s' % (name, origin)


def is_eq(rdataset1, rdataset2):
	if set(rdataset1) == set(rdataset2):
		return True
	for r1 in rdataset1:
		for r2 in rdataset2:
			if r1._cmp(r2):
				break
		else:
			return False
	return True

# resolve nameserver's ip
a = dns.resolver.query('a12-65.akam.net', 'A')
ns_addr = '%s' % a.rrset[0].address
print ns_addr

rlv = dns.resolver.Resolver()
rlv.nameservers = [ns_addr]


ans=rlv.query('myexample.com', 'SOA')
print ans.rrset.name



# read from zonefile
zone = dns.zone.from_file('zone_revised.txt')

# degug show
print 'Origin: ', zone.origin
for name, node in zone.nodes.items():
	#print name, ': '
	for rdataset in node.rdatasets:
		#print dns.rdatatype.to_text(rdataset.rdtype)
		#print name
		ans=rlv.query( fqdn(name, zone.origin), dns.rdatatype.to_text(rdataset.rdtype))
		print 'query: ', ans.rrset
		print 'file : ', fqdn(name, zone.origin), rdataset
		#print set(ans.rrset.items) == set(rdataset.items)
		print	'=>Passed' if is_eq(ans.rrset, rdataset) else '=>NG'
		print
		for rdata in rdataset:
			if rdata.rdtype == dns.rdatatype.A:
				pass
				#print 'A', rdata.address
				#print rdata
			elif rdata.rdtype == dns.rdatatype.NS:
				pass#print 'NS', rdata.target
			elif rdata.rdtype == dns.rdatatype.SOA:
				pass#print 'SOA', rdata.serial
			else:
				pass#print

print '======================'




