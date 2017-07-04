#!/usr/bin/python
from urlparse import urlparse, parse_qs
import BaseHTTPServer
import time

HOST_NAME = '0.0.0.0' 
PORT_NUMBER = 80

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
        
        def do_HEAD(s):
                s.send_response(404)
                s.send_header("Content-type", "text/html")
                s.end_headers()
                
        def do_GET(s):
                """Respond to a GET request."""
                print "GET request"
                s.send_response(200)
                s.send_header("Content-type", "text/html")
                s.end_headers()

                query_components = parse_qs(urlparse(s.path).query)

                print s.headers
                #print query_components
                print urlparse(s.path).query
                for component in query_components.keys():
                        print "component: " + component + " value: " + str(query_components[component])
                print "-------"
                
                s.wfile.write("<html> <body> <h1> Response </h1></body></html>")
                return 
                
        def do_POST(s):
                """Respond to a POST request."""
                print "POST request"
                s.send_response(200)
                s.send_header("Content-type", "text/html")
                s.end_headers()

                length = int(s.headers.getheader('content-length'))
                field_data = s.rfile.read(length)
                query_components = parse_qs(field_data)

                s.wfile.write("<html> <body> <h1> Response </h1></body></html>")
                print s.headers

                for component in query_components.keys():
                        value = query_components[component][0]

                        print "component: " + component + " -- value: " + str(value)          

if __name__ == '__main__':
        server_class = BaseHTTPServer.HTTPServer
        httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
        print time.asctime(), "Inicio - %s:%s" % (HOST_NAME, PORT_NUMBER)
        try:
                httpd.serve_forever()
        except KeyboardInterrupt:
                pass
