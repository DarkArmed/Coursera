'use strict'

angular.module('confusionApp')
  .constant('baseURL', 'http://localhost:3000/')
  .service('menuFactory', ['$resource', 'baseURL', function($resource, baseURL) {

    this.getDishes = function () {
      return $resource(baseURL + 'dishes/:id', null, {'update':{method:'PUT'}});
    };

    this.getPromotions = function () {
      return $resource(baseURL + 'promotions/:id', null, {'update':{method:'PUT'}});
    };

  }])

  .service('corporateFactory', ['$resource', 'baseURL', function($resource, baseURL) {

    this.getLeadership = function () {
      return $resource(baseURL + 'leadership/:id', null, {'update':{method:'PUT'}});
    };

  }])

  .service('feedbackFactory', ['$resource', 'baseURL', function($resource, baseURL) {

    this.getFeedback = function () {
      return $resource(baseURL + 'feedback/:id', null, {'update':{method:'PUT'}});
    };

  }])
;