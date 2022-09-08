import { serve } from "https://deno.land/std/http/server.ts"

const hostname = '127.0.0.1';
const port = 3001;

console.log(`Server running at http://${hostname}:${port}/`);
serve(() => {
    return new Response("Hello, world!", {
        headers: {
            "Content-Type": "text/plain",
        },
    })
}, { hostname, port });
