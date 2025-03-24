from flask import Flask,render_template
PORT= 2100
from lineups import tLineup
from Cards import cards
from signup import signin
from login import logins
from weeklystatistics import weeklystats
from trades import trade
from settings import sett
app = Flask(__name__,template_folder='template')
@app.route("/") 
def index(): 
<<<<<<< HEAD
	return render_template("login.html",login=logins)
=======
	return render_template("settings2.html", settings=sett)

>>>>>>> 8638872e7c3816cd3046cb1b85a31041436bc72e
if __name__ == "__main__": 
	app.run(debug=True, host = '0.0.0.0', port=PORT) 
	app.register_blueprint("home_bp")