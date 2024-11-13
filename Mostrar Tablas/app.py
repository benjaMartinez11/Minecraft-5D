from flask import Flask, jsonify
import mariadb

app = Flask(__name__)

@app.route("/item")
def Order_detail():
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor()
    cur.execute("SELECT * FROM Item")

    items = [column[0] for column in cur.description]
    
    tabla = []
    for row in cur:
        tabla.append(dict(zip(items, row)))

    return jsonify(tabla)

@app.route("/armadura")
def listar_armaduras():
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    cur.execute("SELECT * FROM Armadura")
    tabla = cur.fetchall()

    return jsonify(tabla)

@app.route("/mob")
def listar_mobs():
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    cur.execute("SELECT * FROM Mobs")
    tabla = cur.fetchall()

    return jsonify(tabla)

@app.route("/mob_pass")
def listar_mobs_pass():
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    cur.execute("SELECT * FROM Mob_pass")
    tabla = cur.fetchall()

    return jsonify(tabla)

@app.route("/mob_hostil")
def listar_mobs_hostil():
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    cur.execute("SELECT * FROM Mob_hostil")
    tabla = cur.fetchall()

    return jsonify(tabla)

@app.route("/dimension")
def listas_dimension():
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    cur.execute("SELECT * FROM Dimension")
    tabla = cur.fetchall()

    return jsonify(tabla)

@app.route("/agricultura")
def listas_Agricultura():
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    cur.execute("SELECT * FROM Agricultura")
    tabla = cur.fetchall()

    return jsonify(tabla)

@app.route("/bioma")
def lista_bioma():
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    cur.execute("SELECT * FROM Bioma")
    tabla = cur.fetchall()

    return jsonify(tabla)

@app.route("/caracteristicas_jefe")
def lista_caracteristicas_jefes():
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    cur.execute("SELECT * FROM Caracteristicas_jefe")
    tabla = cur.fetchall()

    return jsonify(tabla)

@app.route("/comida")
def lista_comida():
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    cur.execute("SELECT * FROM Comida")
    tabla = cur.fetchall()

    return jsonify(tabla)

@app.route("/cubos")
def lista_cubos():
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    cur.execute("SELECT * FROM Cubos")
    tabla = cur.fetchall()

    return jsonify(tabla)

