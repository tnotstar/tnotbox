'use strict'

const fetch = require('node-fetch')

const url = 'https://yesno.wtf/api'

fetch(url)
  .then((res) => {
    return res.json()
  })
  .then((json) => {
    console.log(json)
  })
