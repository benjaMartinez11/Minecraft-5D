from flask import Flask, jsonify
import mariadb

app = Flask(__name__)

@app.route("/items")
def Order_detail():
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor()
    cur.execute("SELECT * FROM items")

    items = [column[0] for column in cur.description]
    
    tabla = []
    for row in cur:
        tabla.append(dict(zip(items, row)))

    return jsonify(tabla)


@app.route("/items/<int:id>")
def Tarta(id):
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor()
    cur.execute("SELECT * FROM items WHERE ID= ?", (id,))

    items = [column[0] for column in cur.description]
    
    tabla = [dict(zip(items, row)) for row in cur.fetchall()]

    return jsonify(tabla)
