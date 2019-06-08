const http = require('http')
const socket = require('socket.io')

let httpServer = http.createServer()

httpServer.listen(8088)
ws = socket.listen(httpServer)

setInterval(function () {
    ws.emit('t',new Date().getTime())
},1000)
