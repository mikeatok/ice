from flask import Flask,render_template
PORT= 2000
from lineups import tLineup
from Cards import cards
from signup import signin
from login import logins
from weeklystatistics import weeklystats
from trades import trade

app = Flask(__name__,template_folder='template')
@app.route("/") 
def index(): 
<<<<<<< HEAD
	return render_template("settings.html")
=======
	return render_template("mstats2.html",lineups=tLineup)
>>>>>>> 01e23645f1328f8f45fa975cd72d84a66ef19909
if __name__ == "__main__": 
	app.run(debug=True, host = '0.0.0.0', port=PORT) 
	app.register_blueprint("home_bp")