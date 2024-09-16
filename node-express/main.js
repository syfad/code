//阻塞代码实例

// var fs = require("fs")
//
// var data = fs.readFileSync('input.txt', 'utf-8');
//
// console.log(data, 'end sync read');


// function test()
// {
//     setTimeout(function(){
//         console.log("1001010")
//         test()
//     },5000)
// }
// test()
//
// console.log("程序执行结束")


//非阻塞代码实例
var fs = require("fs");
fs.readFile('input.txt', function (err, data) {
    if (err) return console.error(err);
    console.log(data.toString());
});

console.log("程序执行结束")
