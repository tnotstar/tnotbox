// partially stolen from: https://expressjs.com/en/starter/hello-world.html

const express = require('express')
const app = express()
const port = 3000

app.get('/', async (req, res) => {
    res.send({ greeting: 'Hello, world!' })
})

const start = async () => {
    try {
        await app.listen(port, () => {
            console.log(`Example app listening on port ${port}`)
        })
    } catch (err) {
        app.log.error(err)
        process.exit(1)
    }
}

start()
