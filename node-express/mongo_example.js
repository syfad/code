var MongoClient = require('mongodb').MongoClient;
var DB_CONN_STR = 'mongodb://192.168.100.186:20301,192.168.100.133:20301/space'

var selectData = function (db, callback) {
    var collection = db.collection('activity');

    var whereStr = {"uv":'27'};

    collection.find(whereStr).toArray(function (err, result) {
        if(err)
        {
            console.log('Error:' + err);
            return;
        }
        callback(result);
    });
}

MongoClient.connect(DB_CONN_STR, function (err, db) {
    console.log("connect sucess");
    selectData(db, function (result) {
        console.log(result)
        db.close();
    });
});
