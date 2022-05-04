// partially stolen from: https://www.fastify.io (Request/response validation and hooks)

const Fastify = require('fastify')
const app = Fastify()
const port = 3000

const schema = {
    schema: {
        response: {
            200: {
                type: 'object',
                properties: {
                    greetings: {
                        type: 'string'
                    }
                }
            }
        }
    }
}

app.get('/', schema, async (req, res) => {
    res.send({ greetings: 'Hello, world!' })
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
