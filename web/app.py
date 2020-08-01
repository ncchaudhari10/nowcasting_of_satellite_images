from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#INSAT - 3D
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

if __name__ == "__main__":
    app.run(debug = True)