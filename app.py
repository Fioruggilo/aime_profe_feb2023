# Once activated the environment, install Flask
from flask import Flask, render_template, request, redirect
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Connect to the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aime_profe.db' 
# create the database instance
db = SQLAlchemy(app) 

# create the model for the database table 
class Asistencia(db.Model):

    __tablename__ = 'asistencias'

    id = db.Column(db.Integer, primary_key=True)
    apellido = db.Column(db.String(50), nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    ci = db.Column(db.String(50), nullable=False)
    asistencia = db.Column(db.Integer,  nullable=False)
    grado = db.Column(db.String(20), nullable=False)
    justificativo = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.String(50), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/login', methods = ['GET','POST'])
def login():

    if request.method == 'POST':

        data = request.form
        diccionario_login = data.to_dict(flat=False)
        email= diccionario_login['email'][0]
        password= diccionario_login['password'][0]
        
        if email != '' and password != '' :
    
           return 'Estoy logeado'
    else: 
        return render_template('login.html')
       
    
        #return 'Estoy logeado' #Si quiero ir directo a todo agregar ' redirect(url_for('todo') '

    return render_template('login.html')

@app.route('/<grado>/asistencia/<fecha>', methods=["POST", "GET"])
def asistencia(grado, fecha):

    if request.method == 'POST':
        # Trabajar con el form submit
        print(request.form)
        # return redirect('asistencia')
        return "ok"

    else:
        # return data from the database with SQLALchemy and filter by the parameters
        asistencias = Asistencia.query.filter_by(grado=grado).filter_by(fecha=fecha).all()
        
        return render_template('asistencias.html', asistencias=asistencias)

#execute breakpoint so the debugger is active
if __name__ == '__main__':
    app.run(debug=True)

# use the command python3 app.py to run the app, not flask run

