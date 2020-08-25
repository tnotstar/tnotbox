//
// Sample stolen from:
//   https://www.codementor.io/@rahmanfadhil/build-rest-api-with-express-mongoose-1538dd6c58
//


const dbUrl = "mongodb://localhost:27017/acmedb"
const mongoose = require("mongoose")

mongoose.connect(dbUrl, {
    useNewUrlParser: true,
    useUnifiedTopology: true
})

const express = require("express")
const app = express()

app.listen(5000, () => {
    console.log("Server has started!")
})
