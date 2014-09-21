from flask import Flask, render_template, request 
app = Flask(__name__) 
 
@app.route("/") 
def home(): 
	return render_template('index.html', list=[0,1,2,3,4,5]) 

@app.route("/confirm", methods=['post'])
def confirm():
	print request.form['first_name']
	return render_template('confirm.html')

if __name__ == "__main__": 
    app.run(debug=True) 

