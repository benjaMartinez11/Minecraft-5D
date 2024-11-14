from flask import Flask, jsonify, request
import mariadb


app = Flask(__name__)

@app.route("/item")
def listar_item():
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

#====================================================
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

@app.route("/armadura/<int:id>", methods=('DELETE',))
def borrar_armadura(id):
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    cur.execute("DELETE FROM Armadura WHERE ID = %s", (id,))
    mari.commit()

    return jsonify({"resultado" : "ok",
                    "id" : id})

@app.route("/armadura/", methods=('POST',))
def agregar_armadura():
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    nombre = request.json["nombre"]
    material = request.json["material"]
    durabilidad = request.json["durabilidad"]
    defensa = request.json["defensa"]
    dur_uni = request.json["durabilidad_unidad"]
    consulta = """
        INSERT INTO Armadura (Nombre_armadura, de_que_esta_hecho, durabilidad, 
            defensa, durabilidad_unidad) VALUES (%s, %s, %s, %s, %s)
"""

    cur.execute(consulta, (nombre, material, durabilidad, defensa, dur_uni,))
    mari.commit()
    id = cur.lastrowid

    return jsonify({"resultado" : "ok",
                    "id" : id})

@app.route("/armadura/<int:id>", methods=('PUT',))
def modificar_armadura(id):
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    nombre = request.json["nombre"]
    material = request.json["material"]
    durabilidad = request.json["durabilidad"]
    defensa = request.json["defensa"]
    dur_uni = request.json["durabilidad_unidad"]
    consulta = """
        UPDATE Armadura SET Nombre_armadura = %s, de_que_esta_hecho = %s, 
            durabilidad = %s, defensa=%s, durabilidad_unidad=%s
            WHERE id = %s;
"""

    cur.execute(consulta, (nombre, material, durabilidad, defensa, dur_uni,id))
    mari.commit()

    cur.close()
    mari.close()

    return jsonify({"resultado" : "ok",
                    "id" : id})

#====================================================
#====================================================
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

#====================================================
#====================================================

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

@app.route("/mob_pass/<int:id>", methods=('DELETE',))
def borrar_mob_pass(id):
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    cur.execute("DELETE FROM Mob_pass WHERE ID = %s", (id,))
    mari.commit()

    return jsonify({"resultado" : "ok",
                    "id" : id})

@app.route("/mob_pass/", methods=('POST',))
def agregar_mob_pass():
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    nombre = request.json["nombre"]
    loot = request.json["loot"]
    loot_exp = request.json["loot_exp"]
    vida = request.json["vida"]
    reproduccion = request.json["reproduccion"]
    movilidad = request.json["mivilidad"]
    consulta = """
        INSERT INTO Mob_pass (Nombre_pass, loot, loot_exp, 
            vida, reproduccion, movilidad) VALUES (%s, %s, %s, %s, %s, %s)
"""

    cur.execute(consulta, (nombre, loot, loot_exp, vida,reproduccion, movilidad,))
    mari.commit()
    id = cur.lastrowid

    return jsonify({"resultado" : "ok",
                    "id" : id})

@app.route("/mob_pass/<int:id>", methods=('PUT',))
def modificar_mob_pass(id):
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    nombre = request.json["nombre"]
    loot = request.json["loot"]
    loot_exp = request.json["loot_exp"]
    vida = request.json["vida"]
    reproduccion = request.json["reproduccion"]
    movilidad = request.json["mivilidad"]
    consulta = """
            UPDATE Mob_pass SET Nombre_pass = %s, loot = %s, 
            loot_exp = %s, vida=%s, reproduccion=%s, movilidad=%s
            WHERE id = %s;
"""
    cur.execute(consulta, (nombre, loot, loot_exp, vida,reproduccion, movilidad,))
    mari.commit()

    cur.close()
    mari.close()

    return jsonify({"resultado" : "ok",
                    "id" : id})
#====================================================
#====================================================
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

@app.route("/mob_hostil/<int:id>", methods=('DELETE',))
def borrar_mob_hostil(id):
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    cur.execute("DELETE FROM Mob_pass WHERE ID = %s", (id,))
    mari.commit()

    return jsonify({"resultado" : "ok",
                    "id" : id})

@app.route("/mob_hostil/", methods=('POST',))
def agregar_mob_hostil():
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    nombre = request.json["nombre"]
    loot = request.json["loot"]
    loot_exp = request.json["loot_exp"]
    movilidad = request.json["mivilidad"]
    ataque = request.json["ataque"]
    vida = request.json["vida"]
    distacia = request.json["distancia"]
    consulta = """
        INSERT INTO Mob_hostil (Nombre_hostil, loot, loot_exp, 
            movilidad, ataque, vida, distacia_de_atque) VALUES (%s, %s, %s, %s, %s)
"""

    cur.execute(consulta, (nombre, loot, loot_exp, movilidad, ataque, vida, distacia,id))
    mari.commit()
    id = cur.lastrowid

    return jsonify({"resultado" : "ok",
                    "id" : id})

@app.route("/mob_hostil/<int:id>", methods=('PUT',))
def modificar_mob_hostil(id):
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    nombre = request.json["nombre"]
    loot = request.json["loot"]
    loot_exp = request.json["loot_exp"]
    movilidad = request.json["mivilidad"]
    ataque = request.json["ataque"]
    vida = request.json["vida"]
    distacia = request.json["distancia"]
    consulta = """
        UPDATE Mob_hostil SET Nombre_hostil = %s, loot = %s, 
            loot_exp = %s, movilidad=%s, ataque=%s, vida=%s, distancia_de_ataque=%s,
            WHERE id = %s;
"""
    cur.execute(consulta, (nombre, loot, loot_exp, movilidad, ataque, vida, distacia,id))
    mari.commit()

    cur.close()
    mari.close()

    return jsonify({"resultado" : "ok",
                    "id" : id})
#====================================================
#====================================================
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

@app.route("/dimension/<int:id>", methods=('DELETE',))
def borrar_dimension(id):
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    cur.execute("DELETE FROM Dimension WHERE ID = %s", (id,))
    mari.commit()

    return jsonify({"resultado" : "ok",
                    "id" : id})

@app.route("/dimesion/", methods=('POST',))
def agregar_dimension():
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    nombre = request.json["nombre"]
    descripcion = request.json["descripcion"]
    consulta = """
        INSERT INTO Dimension (nombre_dimesion, descripcion_dimensino ) VALUES (%s, %s)
"""

    cur.execute(consulta, (nombre,descripcion,id))
    mari.commit()
    id = cur.lastrowid

    return jsonify({"resultado" : "ok",
                    "id" : id})

@app.route("/dimension/<int:id>", methods=('PUT',))
def modificar_dimension(id):
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    nombre = request.json["nombre"]
    descripcion = request.json["descripcion"]
    consulta = """
        UPDATE Dimension SET nombre_dimension = %s, descripcion = %s,
            WHERE id = %s;
"""
    cur.execute(consulta, (nombre, descripcion,id))
    mari.commit()

    cur.close()
    mari.close()

    return jsonify({"resultado" : "ok",
                    "id" : id})
#====================================================
#====================================================
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

@app.route("/agricultura/<int:id>", methods=('DELETE',))
def borrar_Agricultura(id):
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    cur.execute("DELETE FROM Agricultura WHERE ID = %s", (id,))
    mari.commit()

    return jsonify({"resultado" : "ok",
                    "id" : id})

@app.route("/agricultura/", methods=('POST',))
def agregar_Agrilcultura():
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    nombre = request.json["nombre"]
    tiempo = request.json["tiempo"]
    loot = request.json["loot"]
    interaccion = request.json["interaccion"]
    consulta = """
        INSERT INTO Agricultura (nombre_semilla, tiempo_de_crecimiento, Loot, Interaccion ) VALUES (%s, %s,%s, %s,%s)
"""

    cur.execute(consulta, (nombre,tiempo,loot, interaccion,id))
    mari.commit()
    id = cur.lastrowid

    return jsonify({"resultado" : "ok",
                    "id" : id})

@app.route("/agricultura/<int:id>", methods=('PUT',))
def modificar_agricultura(id):
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    nombre = request.json["nombre"]
    tiempo = request.json["tiempo"]
    loot = request.json["loot"]
    interaccion = request.json["interaccion"]
    consulta = """
        UPDATE Dimension SET nombre_semilla = %s, tiempo_de_crecimiento = %s, Loot = %s, Interaccion = %s,
            WHERE id = %s;
"""
    cur.execute(consulta, (nombre,tiempo,loot, interaccion,id))
    mari.commit()
    cur.close()
    mari.close()

    return jsonify({"resultado" : "ok",
                    "id" : id})
#====================================================
#====================================================

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

@app.route("/bioma/<int:id>", methods=('DELETE',))
def borrar_bioma(id):
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    cur.execute("DELETE FROM Bioma WHERE ID = %s", (id,))
    mari.commit()

    return jsonify({"resultado" : "ok",
                    "id" : id})

@app.route("/bioma/", methods=('POST',))
def agregar_bioma():
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    nombre = request.json["nombre"]
    consulta = """
        INSERT INTO Agricultura (nombre_bioma ) VALUES (%s)
"""

    cur.execute(consulta, (nombre,id))
    mari.commit()
    id = cur.lastrowid

    return jsonify({"resultado" : "ok",
                    "id" : id})

@app.route("/bioma/<int:id>", methods=('PUT',))
def modificar_bioma(id):
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    nombre = request.json["nombre"]
    consulta = """
        UPDATE Dimension SET nombre_semilla = %s,
            WHERE id = %s;
"""
    cur.execute(consulta, (nombre,id))
    mari.commit()
    cur.close()
    mari.close()

    return jsonify({"resultado" : "ok",
                    "id" : id})

#====================================================
#====================================================

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

@app.route("/caracteristicas_jefe/<int:id>", methods=('DELETE',))
def borrar_caracteristicas_jefe(id):
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    cur.execute("DELETE FROM Caracteristicas_jefe WHERE ID = %s", (id,))
    mari.commit()

    return jsonify({"resultado" : "ok",
                    "id" : id})

@app.route("/caracteristicas_jefe/", methods=('POST',))
def agregar_caracteristicas_jefe():
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    nombre = request.json["nombre"]
    efecto = request.json["efecto"]
    daño_distacia = request.json["daño_distacia"]
    daño_mele = request.json["daño_mele"]
    ataque = request.json["ataque"]
    consulta = """
        INSERT INTO caracteristicas_jefe (nombre_ataque, afecto, daño_a_distacia, daño_mele, daño_del_ataque, jefes_ID ) VALUES (%s, %s, %s, %s, %s, %s)
"""

    cur.execute(consulta, (nombre,efecto,daño_distacia,daño_mele,ataque,id))
    mari.commit()
    id = cur.lastrowid

    return jsonify({"resultado" : "ok",
                    "id" : id})

#====================================================
#====================================================

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

#====================================================
#====================================================

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

#====================================================
#====================================================

@app.route("/estructura")
def lista_estructura():
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    cur.execute("SELECT * FROM Estructura")
    tabla = cur.fetchall()

    return jsonify(tabla)

#====================================================
#====================================================

@app.route("/herramientas_basicas")
def lista_herramientas_basicas():
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    cur.execute("SELECT * FROM Herramientas_basicas")
    tabla = cur.fetchall()

    return jsonify(tabla)

#====================================================
#====================================================

@app.route("/jefes")
def lista_jefes():
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    cur.execute("SELECT * FROM Jefes")
    tabla = cur.fetchall()

    return jsonify(tabla)

#====================================================
#====================================================

@app.route("/jefes_dimension")
def lista_jefes_dimension():
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    cur.execute("SELECT * FROM jefe_dimension")
    tabla = cur.fetchall()

    return jsonify(tabla)

#====================================================
#====================================================

@app.route("/jugador")
def lista_jugador():
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    cur.execute("SELECT * FROM Jugador")
    tabla = cur.fetchall()

    return jsonify(tabla)

#====================================================
#====================================================

@app.route("/zombie_salvador")
def lista_zombie_salvador():
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    cur.execute("SELECT * FROM Zombie_salvador")
    tabla = cur.fetchall()

    return jsonify(tabla)