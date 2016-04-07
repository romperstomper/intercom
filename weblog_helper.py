import argparse
from netaddr import IPSet, IPNetwork
import re

"""Parses a standard HTTP access log and outputs log lines that correspond to a
user request based on either IP address or CIDR range."""

parser = argparse.ArgumentParser(description='Parse HTTP access log')
parser.add_argument('--ip') 


def parselog(ip_addr):
  regex = r'^([\d\.)]+)*'
  ip_addr_set = IPSet(IPNetwork(ip_addr))
  print 'ip_addr_set %s' % ip_addr_set
  with open('/home/gary/Downloads/public_access.log.txt') as fd:
    for index, line in enumerate(fd):
      match = re.search(regex, line)
      if match.group() in ip_addr_set:
        print '%s  %s' % (index, line)
  print 'ip_addr_set len %s' % len(ip_addr_set)

if __name__ == '__main__':
  ip_addr = parser.parse_args().ip
  parselog(ip_addr)
