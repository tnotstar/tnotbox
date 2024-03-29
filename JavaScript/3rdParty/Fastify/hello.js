// partially stolen from: https://www.fastify.io (Quick start)

const Fastify = require('fastify')
const app = Fastify()
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
