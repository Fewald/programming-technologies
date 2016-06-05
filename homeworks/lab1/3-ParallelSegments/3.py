#!/usr/bin/env python
def isLinesCross(x11, y11, x12, y12, x21, y21, x22, y22):
  max_x1 = max(x11, x12)
  max_y1 = max(y11, y12)
  
  min_x1 = min(x11, x12)
  min_y1 = min(y11, y12)
  
  max_x2 = max(x21, x22)
  max_y2 = max(y21, y22)
  
  min_x2 = min(x21, x22)
  min_y2 = min(y21, y22)
  
  if (min_x1 > max_x2 or max_x1 < min_x2 or min_y1 > max_y2 or max_y1 < min_y2):
    return False
  
  dx1 = x12-x11
  dy1 = y12-y11
  
  dx2 = x22-x21
  dy2 = y22-y21
  
  dxx = x11-x21
  dyy = y11-y21
  
  div = dy2*dx1-dx2*dy1
  if (div == 0):
    return False

  if (div > 0):
    mul = dx1*dyy-dy1*dxx
    if (mul < 0 or mul > div):
      return False
	
    mul = dx2*dyy-dy2*dxx
    if (mul < 0 or mul > div):
      return False;
  
  mul = -(dx2*dyy-dy2*dxx)
  if (mul < 0 or mul > -div):
    return False

  mul = -(dx2*dyy-dy2*dxx)
  if (mul > 0 or mul > -div):
    return False
  
  return true


## main
data = input("x11, y11 - x12, y12 - x21, y21 - x22, y22: ")
print isLinesCross(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
#print isLinesCross(data)
