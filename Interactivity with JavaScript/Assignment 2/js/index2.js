/*Add the JavaScript here for the function billingFunction().  It is responsible for setting and clearing the fields in Billing Information */
function billingFunction() {
  var isChecked = document.getElementById('same').checked;
  var billingName = document.getElementById('billingName');
  var billingZip = document.getElementById("billingZip");
  if (isChecked == true) {
    var shippingName = document.getElementById('shippingName');
    var shippingZip = document.getElementById('shippingZip');
    alert("billingname" + shippingName.value);
    billingName.value = shippingName.value;
    billingZip.value = shippingZip.value;
  }
  else{
    billingName.value = "";
    billingZip.value = "";
  }
}