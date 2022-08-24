const PORT = 1337;

var http = require('http');
var url = require('url');
var querystring = require('querystring');
var answer = "none";
const { exec } = require('child_process');

var server = http.createServer(function(req, res) {
    var params = querystring.parse(url.parse(req.url).query);

res.writeHead(200, {"Content-Type": "text/html"});
if ('volume' in params) {
exec('sh setvolume.sh ' + params['volume']);
res.writeHead(302, {'Location': 'Ok'});
}
else if ('button' in params) {
if (params['button'] == 'Up') {
  exec('sh volumeup.sh');
}
else if (params['button'] == 'Down') {
  exec('sh volumedown.sh');
}
res.writeHead(302, {'Location': 'Ok'});
}
