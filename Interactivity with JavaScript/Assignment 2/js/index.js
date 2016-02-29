/*Add the JavaScript here for the function billingFunction().  It is responsible for setting and clearing the fields in Billing Information */

function billingFunction() {
  if (document.getElementById('same').checked) {
    document.getElementById('billingName').value = document.getElementById('shippingName').value;
    document.getElementById('billingZip').value = document.getElementById('shippingZip').value;
    document.getElementById('shippingName').oninput = function () {
      document.getElementById('billingName').value = document.getElementById('shippingName').value;
    };
    document.getElementById('shippingZip').oninput = function () {
      document.getElementById('billingZip').value = document.getElementById('shippingZip').value;      
    };
  } else {
    document.getElementById('billingName').value = '';
    document.getElementById('billingZip').value = '';
    document.getElementById('shippingName').oninput = null;
    document.getElementById('shippingZip').oninput = null;
  }
}