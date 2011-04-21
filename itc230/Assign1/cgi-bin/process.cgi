#!/usr/local/bin/python

# Import modules for CGI handling 
import cgi

# Create instance of FieldStorage 
form = cgi.FieldStorage()

# Get data from fields
first_name = form['first_name'].value
last_name  = form['last_name'].value
email = form['email'].value
phone = form['phone'].value
street_address = form['street_address'].value
suburb = form['suburb'].value
state = form['state'].value
postcode = form['postcode'].value

## Get Order Detail Values
bolt_quantity = form['bolt_quantity'].value
nut_quantity = form['nut_quantity'].value
washer_quantity = form['washer_quantity'].value

bolt_item_price = 2.15
nut_item_price = 0.45
washer_item_price = 0.30

bolt_total = bolt_quantity*bolt_item_price
nut_total = nut_quantity*nut_item_price
washer_total = washer_quantity*washer_item_price

grand_total = bolt_total+nut_total+washer_total


## Get Card Detail Values
card_type = form['card_type'].value
card_name = form['card_name'].value
card_number = form['card_number'].value
security_code = form['security_code'].value
expiry_month = form['expiry_month'].value
expiry_year = form['expiry_year'].value

print "Content-Type: text/html\n\n"
print
print "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\""
print	"\"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">"

print "<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"en\" lang=\"en\">"
print "<head>"
print "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/>"
print "<title>Cart Details - Nuts R Us</title>"
print "<link rel=\"stylesheet\" href=\"/~bchoy02/itc230/assign1/styles/base.css\" />"
print "</head>"

print "<body>"
print "<div id=\"wrapper\">"

print "<div id=\"header\">"
print "<div id=\"logo\"><a href=\"/~bchoy02/itc230/assign1/index.html\">Nuts R Us</a></div>"
print "<div id=\"main-nav\">"
print "<ul>"
print "<li><a href=\"/~bchoy02/itc230/assign1/index.html\">Home</a></li>"
print "<li><a href=\"/~bchoy02/itc230/assign1/about.html\">About Us</a></li>"
print "<li><a href=\"/~bchoy02/itc230/assign1/form.html\">Order Form</a></li>" 
print "<li><a href=\"/~bchoy02/itc230/assign1/contact.html\">Contact Us</a></li>"         
print "</ul>"
print "</div>"
print "</div>"
 
print "<div id=\"container\">"
print "<div class=\"inside\">"
print "<div id=\"content\">"

print "<h1>Your Cart Details</h1>"

print "<h2>Personal Details</h2>"
print "<table>"
print "<tr>"
print "<th>First Name:</th>"
print "<td>%s</td>" %(first_name)
print "</tr>"
print "<tr>"
print "<th>Last Name:</th>"
print "<td>%s</td>" %(last_name)
print "</tr>"
print "<tr>"
print "<th>Email:</th>"
print "<td>%s</td>" %(email)
print "</tr>"
print "<tr>"
print "<th>Phone:</th>"
print "<td>%s</td>" %(phone)
print "</tr>"
print "<tr>"
print "<th>Address:</th>"
print "<td>%s <br />%s <br />%s %s</td>" %(street_address, suburb, state, postcode)
print "</tr>"
print "</table>"

print "<h2>Order Details</h2>"
print "<table>"
print "<thead>"
print "<tr>"
print "<th>Item</th>"
print "<th class=\"nowrap\">Item Price</th>"
print "<th class=\"nowrap\">Ordered Qty</th>"
print "<th>Line Total</th>"
print "</tr>"
print "</thead>"
print "<tfoot>"
print "<tr>"
print "<th colspan=\"3\" align=\"right\">Grand Total</th>"
print "<td>&nbsp; $%s &nbsp;</td>" %(grand_total)
print "</tr>"
print "</tfoot>"
print "<tbody>"
print "<tr>"
print "<th>Bolts:</th>"
print "<td>&nbsp; $%s &nbsp;</td>" %(bolt_quantity)
print "<td>&nbsp; $%s &nbsp;</td>" %(bolt_item_price)
print "<td>&nbsp; $%s &nbsp;</td>" %(bolt_total)
print "</tr>"
print "<tr>"
print "<th>Nuts:</th>"
print "<td>&nbsp; $%s &nbsp;</td>" %(nut_quantity)
print "<td>&nbsp; $%s &nbsp;</td>" %(nut_item_price)
print "<td>&nbsp; $%s &nbsp;</td>" %(nut_total)
print "</tr>"
print "<tr>"
print "<th>Washer:</th>"
print "<td>&nbsp; $%s &nbsp;</td>" %(washer_quantity)
print "<td>&nbsp; $%s &nbsp;</td>" %(washer_item_price)
print "<td>&nbsp; $%s &nbsp;</td>" %(washer_total)
print "</tr>"
print "</tbody>"
print "</table>"

print "<h2>Payment Details</h2>"
print "<table>"
print "<tr>"
print "<th>Card Type:</th>"
print "<td>%s</td>" %(card_type)
print "</tr>"
print "<tr>"
print "<th>Name on Card:</th>"
print "<td>%s</td>" %(card_name)
print "</tr>"
print "<tr>"
print "<th>Card Number:</th>"
print "<td>%s</td>" %(card_number)
print "</tr>"
print "<tr>"
print "<th>Security Code</th>"
print "<td>%s</td>" %(security_code)
print "</tr>"
print "<tr>"
print "<th>Card Expiry:</th>"
print "<td>%s/%s</td>" %(expiry_month, expiry_year)
print "</tr>"
print "</table>"

print "</div>"
print "</div>"
print "</div>"

print "<p class=\"validate\">"
print "<a href=\"http://validator.w3.org/check?uri=referer\">"
print "<img src=\"http://www.w3.org/Icons/valid-xhtml10\" alt=\"Valid XHTML 1.0 Transitional\" height=\"31\" width=\"88\" /></a>"
print "</p>"
print "<p id=\"footer\">Made by Ben Choy for ITC230 Assignment 1</p>"

print "</div>"
print "</body>"
print "</html>"
