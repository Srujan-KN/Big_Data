#!/usr/bin/env python3
"""mapper.py"""

import sys
import json
from datetime import datetime
import math

infile = sys.stdin
w=sys.argv[1]
d=sys.argv[2]
c=0
for line in infile:
	data=json.loads(line)
	key = data["word"]
	if key==w:
		if not (data["word"] != '' and all(chr.isalpha() or chr.isspace() for chr in data["word"])):
			continue
		if not (len(data["countrycode"])==2 and data["countrycode"].isupper()):
			continue
		if not (data["recognized"]==True or data["recognized"]==False):
			continue
		if not (len(data["key_id"])==16 and data["key_id"].isdigit()):
			continue
		if not (len(data["drawing"])>=1 and all(len(i)==2 for i in data["drawing"])):
			continue
		
		x = data["drawing"][0][0][0]
		y = data["drawing"][0][1][0]
		value=0
		try:
			k=int(d)
		except ValueError:
			continue
		if (math.sqrt((x**2)+(y**2)))>k:
			value=1
		country = data["countrycode"]
		print("%s\t%s" % (country,str(value)))
