#!/usr/bin/env python

data=map(int, raw_input("Numbers: ").strip().split(','))
data.sort()
max=list(set(data))

if len(max) > 2:
	print max[-2]
else:
	print 'NO'
exit(0)
