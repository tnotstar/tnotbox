#!/bin/sh
':' //; exec `command -v nodejs || command -v node || command -v js` "$0" "$@"

class Class {
  constructor (attrib = 1.0) {
    this.attrib = attrib
  }
  method() {
    try {
      console.log('This and its attributes are of types: %o and %o',
        typeof this, typeof this.attrib)
      return this.attrib
    } catch(error) {
      console.error('Oops: here we catch a %o', error.name)
    }
  }
}

const unboundGetX = Class.prototype.method
const boundGetX = unboundGetX.bind(new Class(42))
console.log('Bounded = `%o` vs unbounded = `%o`', boundGetX, unboundGetX)

// expected output: 42
console.log('Now, bounded method returns: `%o`', boundGetX())

console.log('Now, unbounded method returns: `%o`', unboundGetX())
// expected output: undefined

// EOF