'use strict'

const Fastify = require('fastify')
const app = Fastify()

const mercurius = require('mercurius')

const schema = `
  type Query {
    add(x: Int, y: Int): Int
  }
`

const addResolver = async (_, {x, y}) => {
    return x + y
}

const resolvers = {
    Query: {
        add: addResolver
    }
}

app.register(mercurius, {
    schema,
    resolvers
})

app.get('/', async function (req, res) {
    const query = '{ add(x: 2, y: 2) }'
    return res.graphql(query)
})

app.listen(3000)
