import os
import tarfile

def getmessage(filepath):

    message = ""
    message += "<html><body>"
    if os.path.isdir(filepath):
        path, dirs, files = next(os.walk(filepath))
        message += "<h3>Files:</h3>"
        for fil in files:
            message += '''<h5><a href=%s/%s>%s</a></h5>'''% (filepath, fil, fil)
        message += "<h3>Folders:</h3>"
        for dirname in dirs:
            message += '''<h5><a href=%s/%s>%s</a></h5>'''% (filepath, dirname, dirname)
    	message += "</body></html>"
        return message                
    if os.path.isfile(filepath):
		if filepath.endswith(".tar"):
			newpath = filepath.replace(".tar","")
		if filepath.endswith(".tar.gz"):
			newpath = filepath.replace(".tar.gz","")
		if filepath.endswith(".tar") or filepath.endswith(".tar.gz"):			
			tar = tarfile.open(filepath)
			#try:
			tar.extractall(path=newpath)
			# except (IOError, OSError) as e:
			# 	pass
			tar.close()
			path, dirs, files = next(os.walk(newpath))
			print files
			for fil in files:
				message += '''<h5><a href=%s/%s>%s</a><h5>'''% (newpath, fil, fil)
			for dirname in dirs:
				message += '''<h5><a href=%s/%s>%s</a><h5>'''% (newpath, dirname, dirname)
			message += "</body></html>"
			return message		
		with open (filepath, "r") as myfile:
		    message += myfile.read().replace('\n','<br />')
		    message += "</body></html>"
    return message
