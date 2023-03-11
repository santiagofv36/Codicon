const express=require('express');
//const http = require("http");
const routerApi=require('./routes');
//const {logerrors,errorhanddler,boomerrorhanddler} =require('./middlewares/error.handle');

const app=express();
const port=3000;

app.use(express.json());

app.get('/',(req,res)=>{
    res.send('Hola mi server en expresssssss')
});

routerApi(app);

/*
app.use(logerrors);
app.use(boomerrorhanddler);
app.use(errorhanddler);
*/

app.listen(port,()=>{
    console.log('App running on port: ',port);
});