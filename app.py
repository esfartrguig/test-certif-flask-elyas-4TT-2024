import os
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    nom = request.form['nom']
    rue = request.form['rue']
    num = request.form['num']
    ville = request.form['ville']
    code = request.form['code']
    data = [nom,rue,num,ville,code]
    file_path = os.path.realpath(__file__)
    work_dir = os.path.dirname(file_path)
    file_csv = f"{work_dir}/data.csv"

    with open(file_csv, "a", encoding="utf-8", newline="") as fichier:
            writer = csv.writer(fichier)
            writer.writerow(data)

    return render_template('result.html', nom=nom)

if __name__ == '__main__':
    app.run(debug=True)