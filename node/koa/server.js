const koa = require('koa')
const router = require('koa-router')
const static = require('koa-static')
const convert = require('koa-convert')
const betterBody = require('koa-better-body')
const session = require('koa-session')
const path = require('path')

const server = new koa()

server.keys=[
    'aaaa','bbbbbb'
]
server.use(session({},server))

server.listen(8080)
let index = router()
server.use(index.routes())
server.use(convert(betterBody(
    {
        uploadDir: path.resolve('../upload')
    }
)))

index.post('/',function (ctx,next) {
    console.log(ctx.request.query)
    ctx.cookies.set('aa',3,{
        maxAge:1
    })
    if (!ctx.session.count) {
        ctx.session.count=1
    }
    else {
        ctx.session.count++
    }
    ctx.response.body = ctx.session.count

})
server.use( async function (ctx,next ) {
    console.log(ctx.params)
    console.log(ctx.request.fields);
    console.log(ctx.request.files);
    ctx.response.body = {
        a: 1
    }
    next()
})

server.use(static(path.resolve('../www')))
