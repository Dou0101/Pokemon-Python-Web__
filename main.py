from flask import *
app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return render_template('index.html')
    
@app.route("/Wobbffet")
def wobbffet():
    return render_template('Wobbffet.html')
    
@app.route("/Pikachu") 
def pikachu():
    return render_template('Pikachu.html')
    
@app.route("/Raichu")
def raichu():
    return render_template('Raichu.html')

@app.route("/Bulbasaur")
def bulbasaur():
    return render_template('Bulbasaur.html')

@app.route("/Download-picture")
def download_picture():
    return render_template('download-picture.html')

@app.route("/Charmander")
def charmander():
    return render_template('Charmander.html')

@app.route("/Squirtle")
def squirtle():
    return render_template('Squirtle.html')

app.run()