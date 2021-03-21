//
// nasa.js - retrieve an image url from NASA's api
//
// Stolen from https://www.twilio.com/blog/2017/08/http-requests-in-node-js.html
//

const http = require("https")
const request = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

http.get(request, (response) => {

    let data = ""

    response.on("data", (chunk) => {
        data += chunk
    })

    response.on("end", () => {
        console.log(JSON.parse(data).explanation)
    })

}).on("error", (err) => {
    console.log("Oops: something is wrong!! (" + err.message + ")")
})

// EOF