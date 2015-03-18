//
// A simple `hello-world` web server
//

import io.vertx.ceylon.platform { ... }
import io.vertx.ceylon.core { ... }
import io.vertx.ceylon.core.http { ... }

shared class Hello() extends Verticle() {
    start(Vertx vertx, Container container) => vertx.createHttpServer().requestHandler(
        void (req) {
            req.response.end("Hello World!");
        }
    ).listen(8080);
}

// EOF
