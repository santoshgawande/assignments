#!/usr/bin/python
# This example written in mod_python to show server time
from mod_python import apache
import datetime

def handler(req):
  req.content_type = 'text/plain'
  t=str(datetime.datetime.now())
  req.write("SERVER TIME:")
  req.write(t)
  return apache.OK
  
