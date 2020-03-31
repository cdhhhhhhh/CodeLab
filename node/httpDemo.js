const http = require('http')
const querying = require('querystring')
const url = require('url')

http.createServer(function (req,res) {

    let { pathname, query} = url.parse(req.url,true)
    console.log(url.parse(req.url,true))

    res.end()
}).listen(8080)

