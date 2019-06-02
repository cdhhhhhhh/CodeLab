const http = require('http');
const fs = require('fs');
const crypto = require('crypto')
const querystring = require('querystring')
const cluster = require('cluster')
const process = require('process')
const Url = require('url')
const mysql = require('mysql')
const socket = require('socket.io')
const uid = require('uuid/v4')
const  zlib = require('zlib')
const db = mysql.createConnection({
    host: 'localhost',
    port: 3306,
    user: 'root',
    password: 'root',
    database: 'test_table'
});

function split(bar, sep) {
    let arr = [];
    let cur = 0;
    let n;
    while ((n = bar.indexOf(sep)) !== -1) {
        arr.push(bar.slice(cur, n));
        bar = bar.slice(n + sep.length)
    }
    arr.push(bar.slice(cur, n));
    return arr
}

function md5(val) {
    let md5 = crypto.createHash('md5');
    md5.update(val);
    return md5.digest('hex');
}

http.createServer((req, res) => {
    if (req.method === 'GET') {
        let {pathname, query} = Url.parse(req.url, true);
        let {name, password} = query;
        switch (pathname) {
            case '/login':
                if (name && password) {
                    db.query(`SELECT * FROM user_table Where name='${name}'`, function (err, data) {
                        if (err) {
                            res.write(`database ${err}`);
                            res.end()
                        } else if (data) {
                            if (data[0].password === password) {
                                res.write('{err:0,msg:\'login success \'}')
                                res.end()

                            } else {
                                res.write('{err:1,msg:\'password error \'}')
                                res.end()
                            }
                        } else {
                            db.query(`INSERT INTO user_table  (id,name,password) VALUES (4234,'${name}','${password}')`, function (data, err) {
                                if (err) {
                                    res.write(`{ err : 1 , msg: \'${err}\' }`)
                                    res.end()
                                } else {
                                    res.write('{ err : 0 , msg: \'username not exist\' }')
                                    res.end()
                                }
                            })

                        }
                    })

                } else {
                    res.write('{ err: 1 ,msg:\'params not incomplete\' }')
                    res.end()
                }
                break;
            case '/reg':
                if (name && password) {
                    db.query(`SELECT * FROM user_table Where name='${name}'`, function (err, data) {
                        if (err) {
                            res.write(`database ${err}`);
                            res.end()
                        } else if (data.length > 0) {
                            res.write('{err:1,msg:\'username exist \'}');
                            res.end()
                        } else {
                            db.query(`INSERT INTO user_table  (id,name,password) VALUES (${Math.random() * 1000000},'${name}','${password}')`, function (err, data) {
                                if (err) {
                                    res.write(`{err:1,msg:\'database ${err}\'}`)
                                    res.end()
                                } else {
                                    if (data) {
                                        res.write('{err:0,msg:\'reg success\'}')
                                        res.end()
                                    }
                                }
                            })
                        }
                    })
                } else {
                    res.write('{err:1,msg:\'params not incomplete\'}')
                    res.end()
                }
                break;
            default:

                let rs = fs.createReadStream(`./www${pathname}`);
                let gz = zlib.createGzip()
                console.log(`./www${pathname}`)
                res.setHeader('content-encoding','gzip')
                rs.pipe(gz).pipe(res)
                rs.on('error', function (err) {
                    console.log(err)
                    res.writeHead(404)
                    res.end('404 Not Find')
                });
        }


    } else if (req.method === 'POST') {

    }


    //文件传输
    // let data = new Buffer('');
    // let Posts = {}
    // req.on('data',(val)=>{
    //     data += val;
    // })
    // req.on('end',()=>{
    //     let str = req.headers['content-type'];
    //     if (str){
    //         let sep = '--'+str.slice(str.indexOf('----'))
    //         arr = split(data,sep)
    //         arr.pop()
    //         arr.shift()
    //         arr = arr.map((res)=>{
    //             return res.slice(2,res.length-2)
    //         })
    //         arr.forEach((item)=>{
    //             let info= split(item,'\r\n\r\n')
    //             console.log(item)
    //
    //             Posts[info[0].slice(info[0].length-9,info[0].length-1)]=info[1].slice(0,info[0].length-1)
    //             console.log(Posts)
    //         })
    //     }
    //     res.end()
    // })
}).listen(8081);

