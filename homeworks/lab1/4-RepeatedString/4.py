#!/usr/bin/env python
import math

data = str(raw_input("String: "));

if not len(data) > 0:
	exit
else:
	length = len(data)
	
	for i in range(1, int(math.ceil(length/2))):
		repeat = int(len(data)/len(data[0:i]))		
		#print 'check ', data[0:i]*repeat
			
		if data[0:i]*repeat == data:
			print data[0:i], ' ', repeat
			exit(0)
print "Fail"
exit(1)
