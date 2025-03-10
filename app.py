from flask import Flask,render_template
PORT= 2100
from Cards import cards
from login import logins

app = Flask(__name__,template_folder='template')

@app.route("/") 
def index(): 
	return render_template("login.html" ,login=logins)

if __name__ == "__main__": 
	app.run(debug=True, host = '0.0.0.0', port=PORT) 
	app.register_blueprint("home_bp")