const  gz = require('zlib')
const  fs = require('fs')

let rs = fs.createReadStream('package.json')
let ws = fs.createWriteStream('test.gz')

rs.pipe(gz.createGzip()).pipe(ws)
