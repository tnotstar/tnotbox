import {serve} from "https://deno.land/std/http/server.ts"

const hostname = '127.0.0.1';
const port = 3001;

const server = serve({hostname: hostname, port: port})
console.log(`Server running at http://${hostname}:${port}/`)
for await (const req of server) {
    const headers = new Headers()
    headers.set("Content-Type", "text/plain")
    req.respond({
        status: 200,
        headers: headers,
        body: "Hello, world!"
    })
}
