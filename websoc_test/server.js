var express = require('express');
const {PythonShell} = require("python-shell");
var app = express();
let options = {
    scriptPath: './',
    args: ["localhost", "3000"]
};
app.get('/', function(req, res){
    // var item = prompt("찾고 싶은 물건 입력: ");
    // options.args.append(item);
    PythonShell.run("websoc_server.py", options, function (err, data) {
        if (err) throw err;
        console.log("받은 데이터 : " + data);
    });
})
var port = options.args[1]
app.listen(port, function () {
    console.log('Connected ' + port)
});
