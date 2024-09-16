var mysql = require('mysql')
var connection = mysql.createConnection({
    host    : '192.168.100.198',
    user    : 'root',
    password: 'root@198.com',
    database: 'mysql',
});

connection.connect();


var sql = 'select user,host,password from user';

connection.query(sql, function (err, result){
    if(err){
        console.log('[SELECT ERROR] - ', err.message);
        return;
    }

    console.log('-----------------SELECT--------------');
    console.log(result);
    console.log('------------------------------------\n\n');
});

connection.end();