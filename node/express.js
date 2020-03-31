const express = require('express')
const body = require('body-parser')
const multer = require('multer')
const cookieParser = require('cookie-parser')
const  cookieSession = require('cookie-session')
let server = express()
server.listen(8082)

server.use(body.urlencoded({extend: false}))
server.use(multer({dest: './upload'}).any())

// server.use(cookieParser('aasdsadasdasddgsahjddghsajgdhasjdghsajdahjsg'))

server.use(cookieSession({
    name:'session',
    keys:['adsadas','dasdas','dasdasdasd'],
}))
server.use(function (req,res,next) {
    console.log('get请求')
    next()
})

server.get('/',function (req,res,next) {

        res.sendFile('/Users/cuidaohan/item/lab/node/www/404.html')
    // res.redirect('https://www.baidu.com')
    // res.setHeader('location','https://www.baidu.com')

    // res.writeHead(401);
    // res.send({a:1,b:4}
    //修改状态

    // res.sendStatus(404)

    // console.log(req.cookies)
    // console.log(req.signedCookies)

    // res.cookie('c',3,{signed:true})
    // res.cookie('c22',4)

})

server.post('/', function (req, res) {
    res.setHeader('Access-Control-Allow-Origin','*')
    console.log(req.body)
    res.send('ok')
})

server.use(express.static('www/'))
