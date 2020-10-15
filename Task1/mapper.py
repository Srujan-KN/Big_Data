#!/usr/bin/env python3
"""mapper.py"""

import sys
import json
from datetime import datetime
import calendar

infile = sys.stdin
w=sys.argv[1]
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
		
		r = data["recognized"]
		value ='0'
		if r:
			value='1'
			#elif findDay(data["timestamp"][:10])=='Sunday' or findDay(data["timestamp"][:10])=='Saturday':
		else:
			date = data["timestamp"][:10]
			x = datetime.strptime(date, '%Y-%m-%d').weekday()
			y = calendar.day_name[x]
			if y=='Sunday' or y=='Saturday':
				value='2'
			
		print("%s\t%s" % (key,value))
