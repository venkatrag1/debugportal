import debugpage

class example_page(debugpage.debugpage):
	def __init__(self):
		self.input_type_name_desc_list = [	('text', 'your_name', 'Enter name here'	), 
											('file', 'test_text_file',  'Select file'	)	]

		debugpage.debugpage.__init__(self, "example_page", "Say hello to", self.input_type_name_desc_list)

	def generate_output(self, input_dict):
		message = "<pre>"
		message += "Hello " + input_dict['text']['your_name'] + "</br>"
		if input_dict['file']['test_text_file'] is not None:
			message += "The contents of the file " + input_dict['file']['test_text_file']['fname'] + " you uploaded is:</br>"
			message += input_dict['file']['test_text_file']['fdata'] 
		message += "</pre>"
		return message


