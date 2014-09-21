from flask import Flask, render_template, request
from key import  ordrin_secret
import ordrin
app = Flask(__name__) 
ordrin_api = ordrin.APIs(ordrin_secret, ordrin.TEST)
 
@app.route("/") 
def home(): 
	return render_template('index.html', list=[0,1,2,3,4,5]) 

@app.route("/confirm", methods=['post'])
def confirm():
	ordrin_api.create_account(request.form['email'], "password", request.form['first_name'], request.form['last_name'])
	
	ordrin_api.create_addr(request.form['email'], "address", request.form['billing_phone_number'], request.form['zip'], 
			request.form['street'], request.form['city'], request.form['state'], "password", addr2=None)
	
	ordrin_api.create_cc(request.form['email'], "card", request.form['credit_card'], request.form['cvc'], 
			request.form['expiration_month'] + "/" + request.form['expiration_year'], request.form['billing_street'], 
			request.form['billing_city'], request.form['billing_state'], request.form['billing_zip'], 
			request.form['billing_phone_number'], "password", bill_addr2=None)
	
	return render_template('confirm.html')

if __name__ == "__main__": 
    app.run(debug=True) 
