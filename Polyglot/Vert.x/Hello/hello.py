#
# A simple `hello-world` web server
#

import vertx

server = vertx.create_http_server()

@server.request_handler
def request_handler(req):
    req.response.end("Hello World!")

server.listen(8080)

# EOF
