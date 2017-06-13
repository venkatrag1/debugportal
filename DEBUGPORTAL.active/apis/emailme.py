import os
import re
import string
import debugpage

ws_dir = debugpage.base_dir + "/emailme"
emailaddr = 'email@email.com'

if not os.path.exists(ws_dir):
	os.makedirs(ws_dir)

def run_service(pathstring):
	decode_str = string.replace(pathstring, "/api/emailme?", "")
	print decode_str
#	str_arr = decode_str.split("&")
#	for item in str_arr:
#		print item
	os.system('echo "%s" | mail -s "Update" %s' % (decode_str, emailaddr))


