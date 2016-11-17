from flask import Flask
from flask import *
from as4 import *

app = Flask(__name__)

@app.route("/")
def bay():
    return render_template("bay.html")

@app.route('/as4/', methods=['POST'])
def hello():
    name=request.form['yourname']
    email=request.form['youremail']
    return render_template('created.html', name=name, email=email)

if __name__ == "__main__":
    app.run()