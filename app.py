from flask import Flask,render_template
PORT= 2100
from Cards import cards
from signup import signin

app = Flask(__name__,template_folder='template')

@app.route("/") 
def index(): 
<<<<<<< HEAD
	return render_template("signup.html" , signup=signin)
=======
	return render_template("index.html", Cards=cards)
>>>>>>> 457e9084bb38efa124828b2efbff6fb2af12fb04

if __name__ == "__main__": 
	app.run(debug=True, host = '0.0.0.0', port=PORT) 
	app.register_blueprint("home_bp")