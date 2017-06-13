import debugpage
import StringIO
import os
import tarfile
import shutil

ws_dir = debugpage.base_dir + "/" + "tarbrowser"
if not os.path.exists(ws_dir):
	os.makedirs(ws_dir)

class tarbrowser(debugpage.debugpage):
	def __init__(self):
		self.input_type_name_desc_list = [	('text', 'filepath', 	'Enter path to the file'),
											('file', 'filename', 'Or Select file from local disk')									]

		ws_dir = debugpage.base_dir + "/" + "tarbrowser"
		if not os.path.exists(ws_dir):
			os.makedirs(ws_dir)
		debugpage.debugpage.__init__(self, "tarbrowser", "Extract tarbrowser", self.input_type_name_desc_list)

	def generate_output(self, input_dict):
		os.chdir(ws_dir)
		file_path = input_dict['text']['filepath']
		if input_dict['file']['filename'] is not None:
			filen = input_dict['file']['filename']['fname']
			data = input_dict['file']['filename']['fdata']
			try:
				open("%s/%s"%(ws_dir,filen), "wb").write(input_dict['file']['filename']['fdata']) 
			except:
				return "Could not upload file"	
			if filen.endswith(".tar"):
				tar = tarfile.open(os.path.join(ws_dir, filen))
				try:
					tar.extractall(path=os.path.join(ws_dir, filen.replace(".tar","")))
				except (IOError, OSError) as e:
					pass
				tar.close()
				os.chdir(os.path.join(ws_dir, filen.replace(".tar","")))
				print os.getcwd()
		elif file_path is not "":
			top_file = os.path.basename(os.path.normpath(file_path)) 
			if os.path.exists(file_path):
				if not os.path.exists(os.path.join(ws_dir, top_file)):
					shutil.copytree(file_path, os.path.join(ws_dir, top_file))
				os.chdir(os.path.join(ws_dir, top_file))
		else:
			return ""
		message = ""
		path = {}
		dirs = {}
		files = {}
		path, dirs, files = next(os.walk(os.getcwd()))
		print files
		print "Files:"
		for fil in files:
			message += '''<h5><a href=%s/%s>%s</a><h5>'''% (os.getcwd(), fil, fil)
		print "Folders:"
		for dirname in dirs:
			message += '''<h5><a href=%s/%s>%s</a><h5>'''% (os.getcwd(), dirname, dirname)		
		return message

