from flask import Flask, render_template, url_for,request
import os
from predictor import predictorsih

app = Flask(__name__)


APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/INSAT-3D/TIR1')
def insat3D_TIR1():
    return render_template('insat3D_TIR1.html')

@app.route('/INSAT-3D/TIR2')
def insat3D_TIR2():
    return render_template('insat3D_TIR2.html')

@app.route('/INSAT-3D/WV')
def insat3D_WV():
    return render_template('insat3D_WV.html')

@app.route('/INSAT-3D/VIS')
def insat3D_VIS():
    return render_template('insat3D_VIS.html')

@app.route('/INSAT-3D/MIR')
def insat3D_MIR():
    return render_template('insat3D_MIR.html')

@app.route('/INSAT-3D/SWIR')
def insat3D_SWIR():
    return render_template('insat3D_SWIR.html')

#3DR
@app.route('/INSAT-3DR/TIR1')
def insat3DR_TIR1():
    return render_template('insat3DR_TIR1.html')

@app.route('/INSAT-3DR/TIR2')
def insat3DR_TIR2():
    return render_template('insat3DR_TIR2.html')

@app.route('/INSAT-3DR/WV')
def insat3DR_WV():
    return render_template('insat3DR_WV.html')

@app.route('/INSAT-3DR/VIS')
def insat3DR_VIS():
    return render_template('insat3DR_VIS.html')

@app.route('/INSAT-3DR/MIR')
def insat3DR_MIR():
    return render_template('insat3DR_MIR.html')

@app.route('/INSAT-3DR/SWIR')
def insat3DR_SWIR():
    return render_template('insat3DR_SWIR.html')
    

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'uploadedData/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)
    predictorsih()
    return render_template("realTimePred.html")

@app.route('/setfile')
def setfile():
    return render_template('upload.html')





if __name__ == "__main__":
    app.run(debug = True)