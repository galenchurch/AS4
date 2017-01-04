from flask import Flask
from flask import *
from as4 import *

app = Flask(__name__)

@app.route("/")
def bay():
    return render_template("bay.html")

@app.route('/as4', methods=['POST', 'GET'])
def hello():
    if request.method=='POST':
        bays = []
        if request.form["bay_wd_1"] != 0:
            curr = request.form["bay_wd_1"]
            print(int(curr))
            bays.append(curr)
            print "bays {}".format(curr)
        if request.form["bay_wd_2"] != '':
            bays.append(request.form["bay_wd_2"])
        if request.form["bay_wd_3"] != '':
            bays.append(request.form["bay_wd_3"])
        if request.form["bay_wd_4"] != '':
            bays.append(request.form["bay_wd_4"])
        if request.form["bay_wd_5"] != '':
            bays.append(request.form["bay_wd_5"])

        for i, x in enumerate(bays):
            if x == '':
                bays.pop(i)
        print bays
        system = as4("N", request.form["mount"], request.form["finish"], 97, 0, bays)
        print system
        return system.genPn()
    else:
        # print request.form
        return render_template("bay.html")

if __name__ == "__main__":
    app.run()