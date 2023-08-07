from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
#sudo apt-get install libmysqlclient-dev
#pip install flask_mysqldb

#from flask_sqlalchemy import SQLAlchemy
#import os
  
#file_path = os.path.abspath(os.getcwd())+"/todo.db"
  
app = Flask(__name__)

#Conexion MySQL
# Conexion MySQL
app.config['MYSQL_HOST'] = '192.168.1.101'
app.config['MYSQL_USER'] = 'app_flask_db'
app.config['MYSQL_PASSWORD'] = 'app_flask_db'
app.config['MYSQL_DB'] = 'app_flask_db'
app.config['MYSQL_PORT'] = 6033



conexion = MySQL(app)


@app.route('/')
def index():
    #return "Hola"
    # return "<h1>UskoKruM2010 - Suscrbete!</h1>"
    cursos = ['A1', 'B1', 'C2', 'D3', 'E5']
    turno = {
        'A': 1,
        'B': 1,
        'C': 1,
        'D': 2
    }

    ventana = [
        'Ventana 1',
        'Ventana 2',
        'Ventana 3'
    ]

    turnoventana = {
        'A1':'Ventana 1',
        'B1':'Ventana 2',
        'C1':'Ventana 3'
    }

    data = {
        'titulo': 'Index123',
        'bienvenida': 'Saludos!',
        'cursos': cursos,
        'numero_cursos': len(cursos)
    }

    return render_template('index.html', data=data)

@app.route('/contacto/<nombre>')
def contacto(nombre):
    data={
        'titulo':'Contacto',
        'nombre':nombre
    }
    return render_template('contacto.html',data=data)

@app.route('/turnero')
def turnero():
    turnero = {}
    try:
        cursor=conexion.connection.cursor()
        sql="select letra, contador from numeros order by letra desc"
        cursor.execute(sql)
        turnero = cursor.fetchall()
        #turnero['turnostupla'] = turnostupla
        #print(turnos)
        #turnos['mensaje'] = 'Turnos'
        type
    except Exception as ex:
        turnero['mensaje'] = 'Error DB'
   # return jsonify(turnos)

    return render_template('turnos.html',turnero=turnero)

@app.route('/administrar', methods=['GET', 'POST'])
def adminturnero():
    if request.method == 'POST':
        action = request.form['action']
        row_id = request.form['row_id']

        if action == 'add_row':
            add_row()
        elif action == 'remove_row':
            remove_row(row_id)
        elif action == 'increment':
            increment_number(row_id)
        elif action == 'decrement':
            decrement_number(row_id)
        elif action == 'set_number':
            new_number = request.form['new_number']
            set_number(row_id, new_number)

    turnero = {}
    try:
        cursor=conexion.connection.cursor()
        sql="select * from numeros order by letra desc"
        cursor.execute(sql)
        turnero = cursor.fetchall()
        cursor.close()
        print(turnero)
        #turnero['turnostupla'] = turnostupla
        #print(turnos)
        #turnos['mensaje'] = 'Turnos'
    except Exception as ex:
        turnero['mensaje'] = 'Error DB'
   # return jsonify(turnos)

    return render_template('adminturnero.html',turnero=turnero)

def add_row():
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO numeros (numero, letra) VALUES (0, 'A')")
    conexion.commit()
    cursor.close()

def remove_row(row_id):
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM numeros WHERE id = %s", (row_id,))
    conexion.commit()
    cursor.close()

def increment_number(row_id):
    cursor = conexion.cursor()
    cursor.execute("UPDATE numeros SET numero = numero + 1 WHERE id = %s", (row_id,))
    conexion.commit()
    cursor.close()

def decrement_number(row_id):
    cursor = conexion.cursor()
    cursor.execute("UPDATE numeros SET numero = numero - 1 WHERE id = %s", (row_id,))
    conexion.commit()
    cursor.close()

def set_number(row_id, new_number):
    cursor = conexion.cursor()
    cursor.execute("UPDATE numeros SET numero = %s WHERE id = %s", (new_number, row_id))
    conexion.commit()
    cursor.close()


###################
    turnero = {}
    try:
        cursor=conexion.connection.cursor()
        sql="select letra, contador from numeros order by letra desc"
        cursor.execute(sql)
        turnero = cursor.fetchall()
        cursor.close()
        #turnero['turnostupla'] = turnostupla
        #print(turnos)
        #turnos['mensaje'] = 'Turnos'
    except Exception as ex:
        turnero['mensaje'] = 'Error DB'
   # return jsonify(turnos)

    return render_template('turnos.html',turnero=turnero)

#from app import routes

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)