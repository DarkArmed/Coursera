var express = require('express');
var bodyParser = require('body-parser');
var mongoose = require('mongoose');

var Promptions = require('../models/promotions');

var promoRouter = express.Router();
promoRouter.use(bodyParser.json());

promoRouter.route('/')
  .get(function (req, res, next) {
    Promptions.find({}, function (err, promotion) {
      if (err) throw err;
      res.json(promotion);
    });
  })
  .post(function (req, res, next) {
    Promptions.create(req.body, function (err, promotion) {
      if (err) throw err;
      console.log('Promotion created!');
      var id = promotion._id;
      res.writeHead(200, {
        'Content-Type': 'text/plain'
      });
      res.end('Added the promotion with id: ' + id);
    });
  })
  .delete(function (req, res, next) {
    Promptions.remove({}, function (err, resp) {
      if (err) throw err;
      res.json(resp);
    });
  });

promoRouter.route('/:promoId')
  .get(function (req, res, next) {
    Promptions.findById(req.params.promoId, function (err, promotion) {
      if (err) throw err;
      res.json(promotion);
    });
  })
  .put(function (req, res, next) {
    Promptions.findByIdAndUpdate(req.params.promoId, {
      $set: req.body
    }, {
      new: true
    }, function (err, promotion) {
      if (err) throw err;
      res.json(promotion);
    });
  })
  .delete(function (req, res, next) {
    Promptions.findByIdAndRemove(req.params.promoId, function (err, resp) {
      if (err) throw err;
      res.json(resp);
    });
  });

module.exports = promoRouter;
