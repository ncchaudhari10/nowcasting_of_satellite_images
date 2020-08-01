from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def insat3D_TIR1():
    return render_template('insat3D_TIR1.html')

@app.route('/INSAT-3D/TIR2')
def insat3D_TIR2():
    return render_template('insat3D_TIR2.html')

if __name__ == "__main__":
    app.run(debug = True)