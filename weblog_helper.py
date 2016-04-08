#!/usr/bin/python
"""Parses a standard HTTP access log and outputs log lines that correspond to a
user request based on either IP address or CIDR range."""

import argparse
from netaddr import IPSet, IPNetwork
import re


parser = argparse.ArgumentParser(description='Parse HTTP access log')
parser.add_argument('--ip', required=True) 
parser.add_argument('--logfile', required=True) 


def parselog(ip_addr, logfile=None):
  """Parses logfile and searches for a specific ip address.

  Args:
    ip_addr: (str) IP address to search for.
    logfile = Abolsute path of logfile to parse.

  Returns:
    (list) Corresponding lines from the logfile that were successfully matched.
  """
  result = []
  regex = r'^([\d\.)]+)*'
  ip_addr_set = IPSet(IPNetwork(ip_addr))
  with open(logfile) as fd:
    for index, line in enumerate(fd):
      match = re.search(regex, line)
      if match.group() in ip_addr_set:
        result.append(line)
  return result


if __name__ == '__main__':
  ip_addr = parser.parse_args().ip
  logfile = parser.parse_args().logfile
  for elem in parselog(ip_addr, logfile=logfile):
    print elem
