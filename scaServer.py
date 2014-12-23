from SimpleHTTPServer import SimpleHTTPRequestHandler
from BaseHTTPServer import BaseHTTPRequestHandler
from BaseHTTPServer import HTTPServer


class MyHTTPRequestHandler( SimpleHTTPRequestHandler ):
    

    def do_POST( self ):
        enc='utf-8'
        self.send_response( 200 )
        self.send_header("Content-type", "text/plain;charset%s" %enc )
        f = open('returnMessage','r')
        ct = f.read()
        self.send_header('Content-length', str(len(ct)))
        self.end_headers()
        self.wfile.write( ct )

    def do_HEAD( self ):
        pass
    

if __name__ == '__main__':
    port = 8080

    handler = SimpleHTTPRequestHandler

    #httpd = SocketServer.TCPServer(("", port ), handler )
    httpd = HTTPServer(('', port ), MyHTTPRequestHandler)

    print "Server is running at port", port
    httpd.serve_forever()
