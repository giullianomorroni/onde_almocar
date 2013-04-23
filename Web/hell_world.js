//Problemas com express no Fedora...criar links para instalação com sudo
//sudo ln -s /usr/local/bin/node /usr/bin/node
//sudo ln -s /usr/local/lib/node /usr/lib/node
//sudo ln -s /usr/local/bin/npm /usr/bin/npm
//sudo ln -s /usr/local/bin/node-waf /usr/bin/node-waf

var express = require('/usr/local/lib/node_modules/express/');
var app = express()
app.set('view engine', 'jade');
app.set('view options', {layout:true});
app.set('views', __dirname + '/views');

app.get('/who/:nome?', function (req, res, next){
  var n = req.params.nome;
  if (n == 'Giulliano') {
    res.render('user', {user:n});
  } else {
    ;;next()
  }
});

app.get('/who/*?', function(req, res){
  res.render('user', {user: null}); ;
});

app.get('/?', function(req, res){
  res.render('index') 
});

var port = 8080
app.listen(port)
console.log('Server running at http://127.0.0.1:'+port+'/');