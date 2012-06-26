'''
Created on Nov 5, 2011

@author: sean
'''

import sys

py2 = sys.version_info[0] < 3
py27 = py2 and sys.version_info[1] >= 7
py3 = not py2

def skip_if(should_skip, message):
	def decorator(method):
		def wrapper(*args, **kwargs):
			if should_skip:
				print message
			else:
				return method(*args, **kwargs)
	return decorator

py2only = skip_if(not py2, "Only valid for python 2.x")

py3only = skip_if(not py3, "Only valid for python 3.x")
