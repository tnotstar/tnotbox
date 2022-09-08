import { serve } from "https://deno.land/std@0.128.0/http/server.ts";

console.log("Running server at http://localhost:8000/");
serve( (req) => new Response("Hello, world!"), { port: 8000 });

