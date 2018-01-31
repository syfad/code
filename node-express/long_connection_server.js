var os = require('os');
var http = require('http');
var fs = require('fs');

var server = http.createServer(function(req, res) {
    if (/^\/a.html/.test(req.url)) {
        fs.createReadStream('a.html').pipe(res);
    } else {
        console.log(req.connection.remoteAddress + ':' + req.connection.remotePort);
        res.writeHead(200, {'Content-Type': 'text/plain'});
        res.end('Hello World\n');
    }
}).listen(8124);
server.setTimeout(0);   //设置不超时，所以服务端不会主动关闭连接

console.log('start ' + os.hostname() + ':8124');