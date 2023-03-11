const express=require('express');
const router=express.Router();
const pool = require('../database');

/*
router.get('/users',(req,res)=>{
  const{limit,offset}=req.query;
  if(limit && offset){
    res.json({
      limit,offset
    })
  }else
    res.send('No hay parametros')
})
*/

router.get('/', async(req, res, next) => {
  const Query = await pool.query("select * from tumama");
  res.json(Query);
});

module.exports=router;