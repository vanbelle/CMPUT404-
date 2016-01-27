#!/usr/bin/env python
# From https://pointlessprogramming.wordpress.com/2011/02/13/python-cgi-tutorial-1/ 2016-01-22
# Copyright Nick Zarczynski

import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()  
 
server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8000)
handler.cgi_directories = ["/"]
 
httpd = server(server_address, handler)
httpd.serve_forever()
Status API Training Shop Blog About Pricing
