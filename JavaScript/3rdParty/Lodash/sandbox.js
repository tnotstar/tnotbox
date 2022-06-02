#!/usr/bin/env node

const _ = require('lodash')

const arrayExamples = function () {
    const data = [null, 2, 0, 4, false, 6, ""]

    console.log(
        '> chunk(%o, 3) -> %o',
        JSON.stringify(data),
        JSON.stringify(_.chunk(data, 3))
    )

    console.log(
        '> compact(%o) -> %o',
        JSON.stringify(data),
        JSON.stringify(_.compact(data))
    )

    console.log(
        '> concat(%o, 1, 2, [3, 4], [[5]]) -> %o',
        JSON.stringify(data),
        JSON.stringify(_.concat(data, 1, 2, [3, 4], [[5]]))
    )
}


console.log(`Beginning lodash version ${_.VERSION} sandbox examples...`)

arrayExamples()

console.log(`Lodash sandbox examples have finished successfully!!`)

// EOF
