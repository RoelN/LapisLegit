#! /usr/bin/env python

import os

for fn in os.listdir('src'):
     if os.path.isfile(fn):
      print (fn)