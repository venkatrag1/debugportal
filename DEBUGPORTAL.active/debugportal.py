from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi
import os
import sys

#Allow for modules to be organized into these folders
dbgportal_dir = os.path.dirname(__file__) or '.'
sys.path.append(os.path.join(dbgportal_dir, 'pages'))
sys.path.append(os.path.join(dbgportal_dir, 'apis'))
sys.path.append(os.path.join(dbgportal_dir, 'helpers'))

import index
import pathparse

class dbgPortalReqHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:

            if self.path.endswith("/"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write('''<html><head><title>Debug Portal!</title>''')
                self.wfile.write(index.create_index_page())
                print index.create_index_page() 
                return
            for key, desc in index.pagelist:
                if self.path.endswith("/" + key):
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    message = ""
                    print(key)
                    print(index.pagemodule[key].get())
                    message += index.pagemodule[key].get()
                    message += "</body></html>"
                    self.wfile.write(message)
                    print message 
                    return
            for key, desc in index.apilist:
                if self.path.startswith("/api/" + key):
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    index.api[key].run_service(self.path)
                    return
            #If not a predefinited path from index or the API list, then invoke pathparse
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(pathparse.getmessage(self.path))             

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        try:
            for key, desc in index.pagelist:
                if self.path.endswith("/" + key):
                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    form = cgi.FieldStorage(
                        fp=self.rfile,
                        headers=self.headers,
                        environ={'REQUEST_METHOD':'POST', 'CONTENT-TYPE':self.headers['Content-type'],})
                    output = ""
                    output += index.pagemodule[key].get()
                    output += index.pagemodule[key].post(form)
                    output += "</body></html>"
                    self.wfile.write(output)


        except:
            pass


def main():
    try:
        port = 8080
        if os.getcwd().endswith('.active'):
            port = 80
        server = HTTPServer(('', port), dbgPortalReqHandler)
        print "Debug Portal running on port %s" % port
        server.serve_forever()
    except KeyboardInterrupt:
        print "stopping Debug Portal"
        server.socket.close()

if __name__ == '__main__':
    main()
