var express = require('express');
var app = express();


// //以下实例中我们引入了 express 模块，并在客户端发起请求后，响应 "Hello World" 字符串
// app.get('/', function (req, res) {
//     res.send('hello world');
//     return res.status(404);
// })
//
// var server = app.listen(8082, function () {
//
//     var host = server.address().address
//     var port = server.address().port
//
//     console.log("应用实例访问地址为: http://%s:%s", host, port)
// })


//路由使用，在HTTP请求中，我们可以通过路由提取出请求的URL以及GET/POST参数

//  主页输出 "Hello World"
app.get('/', function (req, res) {
   console.log("主页 GET 请求");
   res.send('Hello GET');
})


//  POST 请求
app.post('/', function (req, res) {
   console.log("主页 POST 请求");
   res.send('Hello POST');
})

//  /del_user 页面响应
app.get('/del_user', function (req, res) {
   console.log("/del_user 响应 DELETE 请求");
   res.send('delete user');
})

//  /list_user 页面 GET 请求
app.get('/list_user', function (req, res) {
   console.log("/list_user GET 请求");
   res.send('user list pages');
})

// 对页面 abcd, abxcd, ab123cd, 等响应 GET 请求
app.get('/ab*cd', function(req, res) {
   console.log("/ab*cd GET 请求");
   res.send('shell page');
})


var server = app.listen(8081, function () {

  var host = server.address().address
  var port = server.address().port

  console.log("应用实例访问地址：http://%s:%s", host, port)

})


// //你可以使用 express.static 中间件来设置静态文件路径
//
// app.use(express.static('public'))
//
// app.get('/', function (req, res) {
//     res.send('static page');
// })
//
// var server = app.listen(8081, function () {
//     var host = server.address().address
//     var port = server.address().port
//     console.log("access to address: http://%s:%s", host, port)
// })