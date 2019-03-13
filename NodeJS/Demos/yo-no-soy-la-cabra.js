#!/usr/bin/env node
//

parseArguments = function(args) {
    var options = {}

    if(args.length > 2)
        options.inputFilename = args[2].trim()
    else
        throw "Missing command line argument: inputFilename"

    return options
}

findBestSolution = function(options) {
    var data = {}

    if("inputFilename" in options) {
        var inputFilename = options.inputFilename.trim()

        if(inputFilename[0] !== ".")
            inputFilename = "./" + inputFilename
        data = require(inputFilename)
    }

    console.log(JSON.stringify(data))

    return {}
}

printSolution = function(solution) {
    console.log(JSON.stringify(solution))
}

var options = parseArguments(process.argv)
var theBest = findBestSolution(options)

printSolution(theBest)

// EOF