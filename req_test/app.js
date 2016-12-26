var app = require('express')()
app.use(require('body-parser').urlencoded({extended: true}))

app.get('/app', function(req, res){res.send('Get'); } );
app.put('/app', function(req, res){ res.send('Put: a = ' + req.body.a); } );
app.post('/app', function(req, res){ res.send('Post: b = ' + req.body.b); } );
app.delete('/app', function(req, res){ res.send('Delete: c = ' + req.body.c); } );

app.listen(3000, () => { console.log('Listening...'); } );