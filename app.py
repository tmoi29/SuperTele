#Team SuperTele
#Tiffany Moi and Samantha Ngo
#SoftDev1 pd7
#HW05--Jinja Tuning
#2017-09-27

from flask import Flask, render_template
from util import occupation
app = Flask(__name__)

@app.route("/") #home route
def home():
    return 'Check out this cool <a href = "/occupations">page</a>'

@app.route("/occupations") #shows the table
def occupationSetup():
    return render_template('temp.html', dict = occupation.getDict(),length = occupation.getLength(), job = occupation.random_job())

if __name__ == "__main__":
    app.debug = True
    app.run()
