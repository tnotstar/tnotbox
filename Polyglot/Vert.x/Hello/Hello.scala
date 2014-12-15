//
// A simple `hello-world` web server
//

vertx.createHttpServer.requestHandler { req: HttpServerRequest =>
  req.response.end("Hello World!")
}.listen(8080)

// EOF
