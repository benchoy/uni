function validateForm() {
  
  var valid_form = true;
  
  var required_fields=[
    "first_name","last_name", "email", "phone",
    "street_address", "suburb", "state", "postcode",
    "card_type", "card_name", "security_code"
  ];
  
  var quantity_fields=["bolt_quantity", "nut_quantity", "washer_quantity"]
  
  var errcnt = 0;
  var errmsg = "";
  
  // loop through required fields
  for(var i=0; i<required_fields.length; i++) {
    field_name = required_fields[i];
  	var val=document.forms["order_form"][field_name].value
    if (val==null || val=="") {
      errcnt++;
      errmsg += field_name.replace('_', ' ').capitalize()+" must be filled out \n"
    }
  }
  
  if(!validateEmail(document.forms["order_form"]["email"].value)) {
    errcnt++;
    errmsg += "Email must be a valid email address\n";
  }
  
  if(!validatePhone(document.forms["order_form"]["phone"].value)) {
     errcnt++;
     errmsg += "Phone must be a valid phone number with area code\n";
   }
  
  var emtycnt = 0;
  // loop through quantity fields to make sure valid date and ordering of at least 1 item
  for(var i=0; i<quantity_fields.length; i++) {
    field_name = quantity_fields[i];
    var val=document.forms["order_form"][field_name].value
    if(isWholeNumber(val)) {
      if(val==0 || val==null || val=="") {
        emtycnt++; // don't want all items to be empty
      }
    } else {
      errmsg += field_name.replace('_', ' ').capitalize()+" must be a valid whole number \n"
    }
  }
  
  if(emtycnt==3) {
    errcnt++;
    errmsg += "You must order a quantity of at least 1 item\n"
  }
  
  if(errcnt>0) {
    valid_form = false;
    alert(errmsg);
  }
  
  return valid_form;
}

function updateTotals() {

  var quantity_fields=["bolt_quantity", "nut_quantity", "washer_quantity"]
  
  var errmsg = "";
  var errcnt = 0;
  var grand_total = 0;
  
  for(var i=0; i<quantity_fields.length; i++) {
    field_name = quantity_fields[i];
    var val=document.forms["order_form"][field_name].value
    if(!isWholeNumber(val)) {
      errcnt++;
      //errmsg += field_name.replace('_', ' ').capitalize()+" must be a valid whole number \n"
    } else {
      dom_id = field_name.replace('quantity', 'item_price');
      dom_id2 = field_name+"_total";
      item_price = parseFloat(document.getElementById(dom_id).innerHTML);
      field_total = roundNumber(parseInt(val)*item_price, 2);
      grand_total = field_total+grand_total;
      document.getElementById(dom_id2).innerHTML="$"+field_total;
    }
  }
  
  // alert(errcnt);
  if(errcnt > 0) {
    //alert(errmsg);
    document.getElementById("grand_total").innerHTML="You must enter whole numbers";
  } else {
    document.getElementById("grand_total").innerHTML="$"+roundNumber(grand_total, 2);
  }
  
}


// Capitalize function from http://stackoverflow.com/questions/1026069/capitalize-first-letter-of-string-in-javascript
String.prototype.capitalize = function() {
  return this.charAt(0).toUpperCase() + this.slice(1);
}


// Check positive integer http://www.dreamincode.net/code/snippet2758.htm
function isWholeNumber(inputStr) {
    //get the inputStr of the input string
	str = inputStr.toString();
	
	//now we need to loop through the length
	//of the input value
	for(var i=0; i < str.length; i++) {
	    //use charAt to get the current value
		var curValue = str.charAt(i);
		
		//check the value of the current value, if it's less
		//than 0 (zero) and more than 9 we know the value
		//isnt a whole number
		if(curValue < "0" || curValue > "9") {
			return false;	
		}
	}
	return true;
}


// http://forums.devarticles.com/javascript-development-22/javascript-to-round-to-2-decimal-places-36190.html
function roundNumber(num, dec) {
	var result = Math.round(num*Math.pow(10,dec))/Math.pow(10,dec);
	return result;
}

function validateField(val, filter) {
  if (val.match(filter)) {
    return true;
  } else {
    return false;
  }
}

function validateEmail(email) {
  filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
  return validateField(email, filter);
}

function validatePhone(phone) {
  num = phone.replace('(', '').replace(')', '');
  num = num.replace(/ /g,"");
  if(num.length!=10) {
    return false;
  } else {
    return isWholeNumber(num);
  }
}
