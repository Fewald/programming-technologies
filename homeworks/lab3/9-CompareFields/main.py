#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mod

C = mod.Comparator(123)
class Test: pass
T = Test()
T.value = 124
print C.compare(T)