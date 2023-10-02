from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib

# PUT YOUR GLOBAL VARIABLES AND HELPER FUNCTIONS HERE.
# It is not required, but is is strongly recommended that you write a function to parse form data out of the URL, and a second function for generating the contact log page html.

def server(url):
    """
    url is a *PARTIAL* URL. If the browser requests `http://localhost:4131/contact?name=joe#test`
    then the `url` parameter will have the value "/contact?name=joe". So you can expect the PATH
    and any PARAMETERS from the url, but nothing else.

    This function is called each time another program/computer makes a request to this website.
    The URL represents the requested file.

    This function should return two strings in a list or tuple. The first is the content to return
    The second is the content-type.
    """
    #YOUR CODE GOES HERE!

# You shouldn't need to change content below this. It would be best if you just left it alone.

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Call the student-edited server code.
        message, content_type = server(self.path)

        # Convert the return value into a byte string for network transmission
        if type(message) == str:
            message = bytes(message, "utf8")

        # prepare the response object with minimal viable headers.
        self.protocol_version = "HTTP/1.1"
        # Send response code
        self.send_response(200)
        # Send headers
        # Note -- this would be binary length, not string length
        self.send_header("Content-Length", len(message))
        self.send_header("Content-Type", content_type)
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()

        # Send the file.
        self.wfile.write(message)
        return

def run():
    PORT = 4131
    print(f"Starting server http://localhost:{PORT}/")
    server = ('', PORT)
    httpd = HTTPServer(server, RequestHandler)
    httpd.serve_forever()
run()