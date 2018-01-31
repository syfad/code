/**
 * Created by iwang on 2017/1/15.
 */
//express使用的是@4版本的。
var express = require('express');
//form表单需要的中间件。
var mutipart= require('connect-multiparty');

var fs = require("fs");

var mutipartMiddeware = mutipart();
var app = express();
//下面会修改临时文件的储存位置，如过没有会默认储存别的地方，这里不在详细描述。
app.use(mutipart({uploadDir:'/home/wwwroot/branch/jiyu'}));
//设置http服务监听的端口号。
app.set('port',process.env.PORT || 3000);
app.listen(app.get('port'),function () {
    console.log("Express started on http://localhost:"+app.get('port')+'; press Ctrl-C to terminate.');
});
//浏览器访问localhost会输出一个html文件
app.get('/',function (req,res) {
    res.type('text/html');
    res.sendfile('public/index.html')

});
//这里用来玩，express框架路由功能写的，与上传文件没没有关系。
app.get('/about',function (req,res) {
    res.type('text/plain');
    res.send('Travel about');
});
//这里就是接受form表单请求的接口路径，请求方式为post。
app.post('/upload',mutipartMiddeware,function (req,res) {
    //这里打印可以看到接收到文件的信息。
    //console.log(req.files);
    //console.log(req.files['myfile']);
    var oldpath = '/home/wwwroot/branch/jiyu/'
    var original = oldpath + req.files['myfile']['originalFilename']
    var logpath = req.files['myfile']['path']
    //console.log(original);
    //console.log(logpath);
    //console.log(oldpath);
    //console.log(req.files['myfile']['originalFilename']);
    //console.log(req.files['myfile']['path']);
    fs.rename(logpath, original, function (err) {
	if (!err) {
	console.log(original + '替换成功')
	}
})

    /*//do something
    * 成功接受到浏览器传来的文件。我们可以在这里写对文件的一系列操作。例如重命名，修改文件储存路径 。等等。
    *
    *
    * */

    //给浏览器返回一个成功提示。
    res.send('upload success!');
});
