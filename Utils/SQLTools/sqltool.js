
"use strict"

const Token = (type, value=null) => {
    return {type: type, value: value}
}

const ReservedTokens = {
    ".":      Token("Operator", "."),
    ",":      Token("Operator", ","),
    ";":      Token("Operator", ";"),
    __EOF:    Token("Eof"),
    __NAME:   Token("Name"),
    __STRING: Token("String"),
    __NUMBER: Token("Number"),
    as:       Token("Symbol", "AS"),
    select:   Token("Symbol", "SELECT"),
    from:     Token("Symbol", "FROM"),
    where:    Token("Symbol", "WHERE"),
}

const StatementParser = class {

    parse(statement) {
        this.reset(statement)
        let token = this.nextToken()
        while (token !== ReservedTokens.eof) {
            console.log(token)
            token = this.nextToken()
        }
    }

    accept() {
    }

    expect() {
    }

    reset(statement) {
        this.buffer = [...statement]
        this.current = 0
    }

    nextToken() {
        let chr = this.firstChar()

        while (this.isWhiteSpace(chr)) {
            chr = this.nextChar()
        }

        if (this.IsPunctuation(chr)) {
            let buffer = []
            while (this.IsPunctuation(chr)) {
                buffer.push(chr)
                chr = this.nextChar()
            }
            let key = buffer.join("")
            if (key in ReservedTokens)
                return ReservedTokens[key]
        }

        if (this.isNumberStart(chr)) {
            let buffer = []
            while (this.isNumberPart(chr)) {
                buffer.push(chr)
                chr = this.nextChar()
            }
            return Token("Number", Number(buffer.join("")))
        }

        if (this.isIdentifierStart(chr)) {
            let buffer = []
            while (this.isIdentifierPart(chr)) {
                buffer.push(chr)
                chr = this.nextChar()
            }
            let value = buffer.join("")
            let key = value.toLowerCase()
            if (key in ReservedTokens)
                return ReservedTokens[key]
            else
                return Token("Name", value)
        }

        if (chr === '"') {
            let buffer = []
            do {
                chr = this.nextChar()
                if (chr !== '"')
                    buffer.push(chr)
            } while (chr !== '"' && chr !== null)
            if (chr === '"')
                chr = this.nextChar()
            return Token("Name", buffer.join(""))
        }

        if (chr === "'") {
            let buffer = []
            do {
                chr = this.nextChar()
                if (chr !== "'")
                    buffer.push(chr)
            } while (chr !== "'" && chr !== null)
            if (chr === "'")
                chr = this.nextChar()
            return Token("String", buffer.join(""))
        }

        return ReservedTokens.eof
    }

    firstChar() {
        if (this.current < this.buffer.length)
            return this.buffer[this.current]
        return null;
    }

    nextChar() {
        if (this.current < this.buffer.length)
            return this.buffer[++this.current]
        return null;
    }

    isWhiteSpace(chr) {
        return [" ", "\t", "\r", "\n"].includes(chr)
    }

    IsPunctuation(chr) {
        return [".", ",", ";"].includes(chr)
    }

    isNumberStart(chr) {
        return (chr !== null) && ("0" <= chr) && (chr <= "9")
    }

    isNumberPart(chr) {
        return this.isNumberStart(chr) || [".", "e", "E"].includes(chr)
    }

    isIdentifierStart(chr) {
        return (chr !== null) && (('A' <= chr && chr <= 'Z') ||
                ('a' <= chr && chr <= 'z') || (chr === '_'))
    }

    isIdentifierPart(chr) {
        return this.isIdentifierStart(chr) || this.isNumberStart(chr)
    }
}

let parser = new StatementParser()
parser.parse("SELECT 'Hello, world!'")
parser.parse("SELECT name FROM customer")
parser.parse("SELECT c.name FROM customer AS c")
