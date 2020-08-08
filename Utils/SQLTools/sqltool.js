
"use strict"

const Token = (type, value=null) => {
    return {type: type, value: value}
}

const ReservedTokens = {
    '"':    Token("symbol", '"'),
    "'":    Token("symbol", "'"),
    ".":    Token("symbol", "."),
    ",":    Token("symbol", ","),
    ";":    Token("symbol", ";"),
    nil:    Token("nil"),
    ident:  Token("symbol"),
    AS:     Token("symbol", "as"),
    SELECT: Token("symbol", "select"),
    FROM:   Token("symbol", "from")
}

const StatementParser = class {

    parse(statement) {
        this.reset(statement)
        let token = this.nextToken()
        while (token !== ReservedTokens.nil) {
            console.log(token)
            token = this.nextToken()
        }
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

        if (this.isNumber(chr)) {
            let buffer = []
            while (this.isNumber(chr)) {
                buffer.push(chr)
                chr = this.nextChar()
            }
            return Token("number", Number(buffer.join("")))
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

        if (this.isIdentifier(chr)) {
            let buffer = []
            while (this.isIdentifier(chr)) {
                buffer.push(chr)
                chr = this.nextChar()
            }
            let key = buffer.join("")
            if (key in ReservedTokens)
                return ReservedTokens[key]
            else
                return Token("ident", key)
        }
        return ReservedTokens.nil
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

    isNumber(chr) {
        return '0' <= chr && chr <= '9'
    }

    IsPunctuation(chr) {
        return [",", "'", '"'].includes(chr)
    }

    isIdentifier(chr) {
        return ('A' <= chr && chr <= 'Z') ||
                ('a' <= chr && chr <= 'z') ||
                (chr === '_')
    }
}

let parser = new StatementParser()
parser.parse("SELECT 'Hello, world!'")
