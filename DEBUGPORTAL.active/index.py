#HTML pages for debugcentral
pagelist = [
			#	("example_page", 	"Hello world example as a started for building page"),
				("tarbrowser",		"Extract and explore tar files"),
			]


#API endpoints for debugcentral
apilist       = [
					("emailme",		"Send email notification"),
				]

####

##Implementation

pagemodule = {}
for key, desc in pagelist:
	try: 
		pagemodule[key] = getattr(__import__(key), key)()
	except ImportError:
		pagemodule[key] = None


modlist_entry = '''<li><a href="{entry}">{entry_desc}</a></li>'''

def create_index_page():
	page_str = ""
	page_str += "<body><h2>Debug Portal</h2><ol>"
	for key, desc in pagelist:
		page_str += modlist_entry.format(
			entry=key,
			entry_desc=desc)
	page_str += "</ol></body></html>"
	return page_str

#####
api = {}

for key, desc in apilist:
	try:
		api[key] = __import__(key)
	except ImportError:
		api[key] = {}




