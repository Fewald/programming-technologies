#!/usr/bin/env python
input_object = raw_input("Enter your object: ")

for attr in dir(input_object):
  if (not attr.startswith('__')):
    print attr
