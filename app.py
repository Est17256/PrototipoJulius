
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'DB://User:Pass@Host:Port/Name'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'
db = SQLAlchemy(app)
class PersonaDemo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True, nullable=False)
    apellido = db.Column(db.String(120), nullable=False)
    def __init__(self, nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
@app.route('/')
def home():
    return '<a href="/addperson"><button>Iniciar</button></a>'
@app.route("/addperson")
def addperson():
    return render_template("index.html")
@app.route("/personadd", methods=['POST'])
def personadd():
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    entry = PersonaDemo(nombre,apellido)
    db.session.add(entry)
    db.session.commit()
    return render_template("index.html")
if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0',port=80)