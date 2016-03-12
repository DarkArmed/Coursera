'use strict';

describe('conFusion App E2E Testing', function () {

  it('should automatically redirect to / when location hash/fragment is empty', function () {

    browser.get('index.html');
    expect(browser.getLocationAbsUrl()).toMatch("/");

  });

  describe('index', function () {
    beforeEach(function () {
      browser.get('index.html#/');
    });

    it('should have a title', function () {
      expect(browser.getTitle())
        .toEqual('Ristorante Con Fusion');

    });
  });

  describe('menu 0 item', function () {
    beforeEach(function () {
      browser.get('index.html#/menu/0');
    });

    it('should have a name', function () {
      var name = element(by.binding('dish.name'));
      expect(name.getText())
        .toEqual('Uthapizza Hot $4.99');

    });

    it('should show the number of comments as', function () {
      expect(element.all(by.repeater('comment in dish.comments'))
        .count()).toEqual(7);

    });

    it('should show the first comment author as', function () {
      element(by.model('orderText')).sendKeys('author');
      expect(element.all(by.repeater('comment in dish.comments'))
        .count()).toEqual(7);
      var author = element.all(by.repeater('comment in dish.comments'))
        .first().element(by.binding('comment.author'));

      expect(author.getText()).toContain('25 Cent');

    });
  });

  describe('feedback', function () {
    var firstName = element(by.model('feedback.firstName'));
    var lastName = element(by.model('feedback.lastName'));
    var areaCode = element(by.model('feedback.tel.areaCode'));
    var number = element(by.model('feedback.tel.number'));
    var email = element(by.model('feedback.email'));
    var agree = element(by.model('feedback.agree'));
    var mychannel = element(by.model('feedback.mychannel'));
    var comments = element(by.model('feedback.comments'));
    var submit = element(by.id('sendfeedback'));


    beforeEach(function () {
      browser.get('index.html#/contactus');
    });

    it('should clear the form after submit', function () {
      firstName.sendKeys('Miaoji');
      lastName.sendKeys('Heng');
      areaCode.sendKeys('123');
      number.sendKeys('4567890');
      email.sendKeys('miaoji@heng');
      agree.click();
      browser.driver.wait(protractor.until.elementIsVisible(mychannel))
      mychannel.sendKeys('Email');
      comments.sendKeys('屌屌哒~~~');

      expect(firstName.getAttribute('value')).toEqual('Miaoji');
      
      browser.sleep(1000);

      submit.click();

      expect(firstName.getAttribute('value')).toEqual('');

    });
  });

});