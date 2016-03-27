var mongoose = require('mongoose')
  , assert = require('assert');

var Dishes = require('./models/dishes');
var Promotions = require('./models/promotions');
var Leadership = require('./models/leadership');

// Connection URL
var url = 'mongodb://localhost:27017/conFusion';
mongoose.connect(url);
var db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function () {
  // we're connected!
  console.log("Connected correctly to server");

  // create a new user
  Dishes.create({
    name: 'Uthapizza',
    image: 'images/uthapizza.png',
    category: 'mains',
    price: '4.99',
    description: 'A unique . . .',
    comments: [
      {
        rating: 5,
        comment: 'Imagine all the eatables, living in conFusion!',
        author: 'John Lemon'
      }
    ]
  }, function (err, dish) {
    if (err) throw err;

    console.log('Dish created!');
    console.log(dish);
    
    var id = dish._id;

    //get all the dishes
    setTimeout(function () {
      Dishes.findByIdAndUpdate(id, {
        $set: {
          label: 'Hot'
        }
      } ,{
        new: true
      })
      .exec(function (err, dish) {
        if (err) throw err;
        console.log('Updated Dish!');
        console.log(dish);

        setTimeout(function (){
          dish.comments.push({
            rating: 4,
            comment: 'Sends anyone to heaven, I wish I could get my mother-in-law to eat it!',
            author: 'Paul McVites'
          });
          
          dish.save(function (err, dish) {
            console.log('Updated Comments!');
            console.log(dish);
            db.collection('dishes').drop(function () {
              Promotions.create({
                name: 'Weekend Grand Buffet',
                image: 'images/buffet.png',
                price: '19.99',
                description: 'Featuring . . .'
              }, function (err, promotion) {
                if (err) throw err;

                console.log('Promotion created!');
                console.log(promotion);
                
                var id = promotion._id;

                //get all the promotions
                setTimeout(function () {
                  Promotions.findByIdAndUpdate(id, {
                    $set: {
                      label: 'New'
                    }
                  } ,{
                    new: true
                  })
                  .exec(function (err, promotion) {
                    if (err) throw err;
                    console.log('Updated Promotion!');
                    console.log(promotion);

                    db.collection('promotions').drop(function () {
                      Leadership.create({
                        name: 'Peter Pan',
                        image: 'images/alberto.png',
                        designation: 'Chief Epicurious Officer',
                        abbr: 'CEO',
                        description: 'Our CEO, . . .'
                      }, function (err, leader) {
                        if (err) throw err;

                        console.log('Leader created!');
                        console.log(leader);
                        
                        var id = leader._id;

                        //get all the leaders
                        setTimeout(function () {
                          Leadership.findByIdAndUpdate(id, {
                            $set: {
                              description: 'Our CEO, Peter, . . .'
                            }
                          } ,{
                            new: true
                          })
                          .exec(function (err, leader) {
                            if (err) throw err;
                            console.log('Updated Leader!');
                            console.log(leader);

                            db.collection('leaders').drop(function () {
                              db.close();
                            });
                          });
                        }, 1000);
                      });
                    });
                  });
                }, 1000);
              });
            });
          });
        }, 1000);
      });
    }, 1000);
  });
});