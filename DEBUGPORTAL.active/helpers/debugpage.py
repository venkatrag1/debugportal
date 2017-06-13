import webbrowser

base_dir = "~/FileStore"

class debugpage:

    """
    Baseclass that can be subclassed by all Pages. Constructor takes the following arguments
    1) Page name as used in the index.pagelist
    2) Title string for that page
    3) A list of triples containing for each field of input, the type (file/text) of input, the identifier string and description string

    Refer to example_page.py for an example of how to create the subclass pages
    All page subclasses will override the generate_output method

    """
    def __init__(self, page_name, page_heading, input_type_name_desc):

        #tagstr = '''<html><script src="http://code.jquery.com/jquery-1.10.1.min.js"></script></head><script type="text/javascript" charset="utf-8">$(document).on("click", "#bmcnum", function(event) {$("#filename").prop("disabled", true);$("#bmcnum").prop("disabled",false);});$(document).on("click", "#filename", function(event) {$("filename").prop("disabled", false);$("#bmcnum").prop("disabled", true);});}</script>'''
        tagstr = '''<html>'''
        self.page_heading = "%s<body><h2>%s</h2>" % (tagstr, page_heading)
        self.inputs = input_type_name_desc
        self.form_input = "<form method='POST' enctype='multipart/form-data' action='/%s'>" % page_name
        for (input_type, input_name, input_desc) in self.inputs:
            self.form_input += "<h3>%s</h3>" % input_desc
            self.form_input += "<input name='%s' id ='%s' type='%s'>" % (input_name, input_name, input_type)
        self.form_input += '''<input type="submit" value="Submit"> </form>'''
        self.get_output = self.page_heading + self.form_input


    def get(self):

        """
        HTTP GET RESPONSE
        """
        return self.get_output

    def post(self, form):
        """
        HTTP POST RESPONSE
        """
        input_dict = {}
        input_dict['file'] = {}
        input_dict['text'] = {}
        for (input_type, input_name, input_desc) in self.inputs:
            (filen, filedata) = ("", "")
            if input_type == 'file':
                filen = form[input_name].filename
                if filen is not "":
                    filedata = form[input_name].file.read()
                    input_dict[input_type][input_name] = {'fname': filen, 'fdata': filedata}
                else:
                    input_dict[input_type][input_name] = None
            elif input_type == 'text':
                input_dict[input_type][input_name] = form.getvalue(input_name)
        return self.generate_output(input_dict)

    def generate_output(self, input_dict):
        message = "<pre>"
        for (input_type, input_name, input_desc) in self.inputs:
            if input_type == 'file' and input_dict[input_type][input_name] is not None:
                print "file name is " + input_dict[input_type][input_name]['fname']
                message += "Filename for %s field is: %s</br>" % (input_name, input_dict[input_type][input_name]['fname'])
                message += "Data is " + input_dict[input_type][input_name]['fdata']
            elif input_type == 'text':
                print "text is " + input_dict[input_type][input_name]
                message += "Text for %s field is: %s" % (input_name, input_dict[input_type][input_name])
            message += "</br>"
        message += "</pre>"
        return message


