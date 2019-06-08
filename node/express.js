const express = require('express')
const body = require('body-parser')
const multer = require('multer')

let server = express()
server.listen(8082)

server.use(body.urlencoded({extend: false}))
server.use(multer({dest: './upload'}).any())

server.post('/', function (req, res) {
    res.setHeader('Access-Control-Allow-Origin','*')
    console.log(req.body)
    res.send('ok')
})
