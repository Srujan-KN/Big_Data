#!/usr/bin/env python3
"""reducer.py"""

from operator import itemgetter
import sys

current_word = sys.argv[1]
current_count_1 = 0
current_count_2 = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    	# remove leading and trailing whitespace
    	line = line.strip()

    	# parse the input we got from mapper.py
    	word, val = line.split('\t', 1)

    	# convert count (currently a string) to int
    	#if key==w:
    	try:
    		count = int(val)
    	except ValueError:
    		continue
    	if current_word == word:
    		if count==1:
    			current_count_1 += count
    		elif count==2:
    			current_count_2 += 1
    	else:
    		print('%s\t%s\t%s' % (current_word, str(current_count_1),str(current_count_2)))
    		#current_count_1 = 0
    		#current_count_2 = 0
    		#current_word = word
if current_word == word:
    	#print('%s\t%s\t%s' % (current_word, current_count_1, current_count_2))
    	print('%s\n%s' % (current_count_1, current_count_2))
