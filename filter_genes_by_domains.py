#!/usr/bin/python

import os, sys, re

X=["TIR", "TIR2", "LRR", "LRR_8", "Rx_N","RPW8"]


input = open(sys.argv[1])

for line in input:
	line=line.rstrip().replace("~", " ").replace(", ", "XXX")
	if line=="":
		continue
	#print line
	linearray=line.split()
	genename=linearray[0]
	Xdomain=set()
	nonXdomain=0
	NBARC=set()
	for domain in linearray[1:]:
		found=False
		if domain.startswith("NB-ARC"):
			NBARC.add("NB-ARC")
			found=True
		if found==True:
			continue

		for x in X:
			if domain.startswith(x):
				Xdomain.add(x)
				found = True
				break
		if found==True:
			continue
		else:
			nonXdomain+=1
	#print "Xdomain", Xdomain, len(Xdomain), "nonXdomain", nonXdomain
	if len(linearray) == 3: #one NBARC, one genename, one domain
		if len(Xdomain) > 0 and len(NBARC) > 0:
			pass
	if nonXdomain > 0 and len(NBARC) > 0:
		print line.replace("XXX", ", ")
	elif nonXdomain > 0:
		print line.replace("XXX", ", ")

exit(0)
