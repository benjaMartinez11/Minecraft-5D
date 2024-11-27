from flask import Flask, jsonify, request, Flask, render_template, Blueprint
from flask_cors import CORS
import mariadb
bp = Blueprint()
app = Flask(__name__)

#---------------------------------------------------------
#---------------------NUEVO-------------------------------
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

    return render_template("item.html", tablas = tabla)

#=======================================

@app.route("/api/item")
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
@app.route("/api/armadura")
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

    return render_template(tabla)

@app.route("/api/armadura/<int:id>", methods=('DELETE',))
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

#====================================================

@app.route("/api/armadura/", methods=('POST',))
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
        INSERT INTO Armadura (nombre_armadura, de_que_esta_hecho, durabilidad, 
            defensa, durabilidad_unidad) VALUES (%s, %s, %s, %s, %s)
"""

    cur.execute(consulta, (nombre, material, durabilidad, defensa, dur_uni,))
    mari.commit()
    id = cur.lastrowid

    return jsonify({"resultado" : "ok",
                    "id" : id})

#====================================================

@app.route("/api/armadura/<int:id>", methods=('PUT',))
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
        UPDATE Armadura SET nombre_armadura = %s, de_que_esta_hecho = %s, 
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
@app.route("/api/mob")
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

@app.route("/api/mob_pass")
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

@app.route("/api/mob_pass/<int:id>", methods=('DELETE',))
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

@app.route("/api/mob_pass/", methods=('POST',))
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

@app.route("/api/mob_pass/<int:id>", methods=('PUT',))
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
@app.route("/api/mob_hostil")
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

@app.route("/api/mob_hostil/<int:id>", methods=('DELETE',))
def borrar_mob_hostil(id):
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    cur.execute("DELETE FROM Mob_hostil WHERE ID = %s", (id,))
    mari.commit()

    return jsonify({"resultado" : "ok",
                    "id" : id})

@app.route("/api/mob_hostil/", methods=('POST',))
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
        INSERT INTO Mob_hostil (nombre_hostil, loot, loot_exp, 
            movilidad, ataque, vida, distacia_de_atque) VALUES (%s, %s, %s, %s, %s)
"""

    cur.execute(consulta, (nombre, loot, loot_exp, movilidad, ataque, vida, distacia,id))
    mari.commit()
    id = cur.lastrowid

    return jsonify({"resultado" : "ok",
                    "id" : id})

@app.route("/api/mob_hostil/<int:id>", methods=('PUT',))
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
        UPDATE Mob_hostil SET nombre_hostil = %s, loot = %s, 
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
@app.route("/api/mob_neutro")
def listar_mobs_neutro():
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    cur.execute("SELECT * FROM Mob_neutro")
    tabla = cur.fetchall()

    return jsonify(tabla)

@app.route("/api/mob_neutro/<int:id>", methods=('DELETE',))
def borrar_mob_neutro(id):
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    cur.execute("DELETE FROM Mob_neutro WHERE ID = %s", (id,))
    mari.commit()

    return jsonify({"resultado" : "ok",
                    "id" : id})

@app.route("/api/mob_neutro/", methods=('POST',))
def agregar_mob_neutro():
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
    reproduccion = request.json["reproduccion"]
    movilidad = request.json["mivilidad"]
    ataque = request.json["ataque"]
    vida = request.json["vida"]
    consulta = """
        INSERT INTO Mob_neutro (nombre_neutro, loot, loot_exp, 
            reproduccion ,movilidad, ataque, vida) VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

    cur.execute(consulta, (nombre, loot, loot_exp, movilidad, ataque, vida, reproduccion,id))
    mari.commit()
    id = cur.lastrowid

    return jsonify({"resultado" : "ok",
                    "id" : id})

@app.route("/api/mob_neutro/<int:id>", methods=('PUT',))
def modificar_mob_neutro(id):
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
    reproduccion = request.json["reproduccion"]
    consulta = """
        UPDATE Mob_hostil SET nombre_hostil = %s, loot = %s, 
            loot_exp = %s, movilidad=%s, ataque=%s, vida=%s, reproduccion=%s,
            WHERE id = %s;
"""
    cur.execute(consulta, (nombre, loot, loot_exp, movilidad, ataque, vida, reproduccion,id))
    mari.commit()

    cur.close()
    mari.close()

    return jsonify({"resultado" : "ok",
                    "id" : id})
#====================================================
#====================================================
@app.route("/api/dimension")
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

@app.route("/api/dimension/<int:id>", methods=('DELETE',))
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

@app.route("/api/dimesion/", methods=('POST',))
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

@app.route("/api/dimension/<int:id>", methods=('PUT',))
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
@app.route("/api/agricultura")
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

@app.route("/api/agricultura/<int:id>", methods=('DELETE',))
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

@app.route("/api/agricultura/", methods=('POST',))
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

@app.route("/api/agricultura/<int:id>", methods=('PUT',))
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
        UPDATE Agriculturas SET nombre_semilla = %s, tiempo_de_crecimiento = %s, Loot = %s, Interaccion = %s,
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

@app.route("/api/bioma")
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

@app.route("/api/bioma/<int:id>", methods=('DELETE',))
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

@app.route("/api/bioma/", methods=('POST',))
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
        INSERT INTO Bioma (nombre_bioma ) VALUES (%s)
"""

    cur.execute(consulta, (nombre,id))
    mari.commit()
    id = cur.lastrowid

    return jsonify({"resultado" : "ok",
                    "id" : id})

@app.route("/api/bioma/<int:id>", methods=('PUT',))
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
        UPDATE Bioma SET nombre_bioma = %s,
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

@app.route("/api/caracteristicas_jefe")
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

@app.route("/api/caracteristicas_jefe/<int:id>", methods=('DELETE',))
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

@app.route("/api/caracteristicas_jefe/", methods=('POST',))
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
        INSERT INTO Caracteristicas_jefe (nombre_ataque, afecto, daño_a_distacia, daño_mele, daño_del_ataque, jefes_ID ) VALUES (%s, %s, %s, %s, %s, %s)
"""

    cur.execute(consulta, (nombre,efecto,daño_distacia,daño_mele,ataque,id))
    mari.commit()
    id = cur.lastrowid

    return jsonify({"resultado" : "ok",
                    "id" : id})

@app.route("/api/caracteristicas_jefe/<int:id>", methods=('PUT',))
def modificar_caracteristicas_jefe(id):
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
        UPDATE Caracteristicas_jefe SET nombre_ataque = %s, afecto =%s, daño_a_distacia =%s, daño_mele =%s, daño_del_ataque =%s,
            WHERE id = %s;
"""
    cur.execute(consulta, (nombre,efecto,daño_distacia,daño_mele,ataque,id))
    mari.commit()
    cur.close()
    mari.close()

    return jsonify({"resultado" : "ok",
                    "id" : id})

#====================================================
#====================================================

@app.route("/api/comida")
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

@app.route("/api/comida/<int:id>", methods=('DELETE',))
def borrar_comida(id):
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    cur.execute("DELETE FROM Comida WHERE ID = %s", (id,))
    mari.commit()

    return jsonify({"resultado" : "ok",
                    "id" : id})

@app.route("/api/comida/", methods=('POST',))
def agregar_comida():
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    nombre = request.json["nombre"]
    efecto = request.json["efecto"]
    saturacion = request.json["saturacion"]
    recuperar_vida = request.json["recuperar_vida"]
    receta = request.json["receta"]
    consulta = """
        INSERT INTO Comida (nombre_comida, afecto, recuperar_hambre, recuperar_vida, receta) VALUES (%s, %s, %s, %s, %s)
"""

    cur.execute(consulta, (nombre, efecto, saturacion, recuperar_vida, receta, id))
    mari.commit()
    id = cur.lastrowid

    return jsonify({"resultado" : "ok",
                    "id" : id})

@app.route("/api/comida/<int:id>", methods=('PUT',))
def modificar_comida(id):
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    nombre = request.json["nombre"]
    efecto = request.json["efecto"]
    saturacion = request.json["saturacion"]
    recuperar_vida = request.json["recuperar_vida"]
    receta = request.json["receta"]
    consulta = """
        UPDATE Comida SET nombre_comida = %s, afecto =%s, recuperacion_hambre =%s, recuperar_vida =%s, receta =%s,
            WHERE id = %s;
"""
    cur.execute(consulta, (nombre, efecto, saturacion, recuperar_vida, receta, id))
    mari.commit()
    cur.close()
    mari.close()

    return jsonify({"resultado" : "ok",
                    "id" : id})
#====================================================
#====================================================

@app.route("/api/cubos")
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

@app.route("/api/cubos/<int:id>", methods=('DELETE',))
def borrar_cubos(id):
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    cur.execute("DELETE FROM Cubos WHERE ID = %s", (id,))
    mari.commit()

    return jsonify({"resultado" : "ok",
                    "id" : id})

@app.route("/api/cubos/", methods=('POST',))
def agregar_cubos():
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    nombre = request.json["nombre"]
    capacidad = request.json["capacidad"]
    interaccion = request.json["interaccion"]
    consulta = """
        INSERT INTO Cubos (nombre_cubo, capacidad, interaccion) VALUES (%s, %s, %s)
"""

    cur.execute(consulta, (nombre, capacidad, interaccion, id))
    mari.commit()
    id = cur.lastrowid

    return jsonify({"resultado" : "ok",
                    "id" : id})

@app.route("/api/cubos/<int:id>", methods=('PUT',))
def modificar_cubos(id):
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    nombre = request.json["nombre"]
    capacidad = request.json["capacidad"]
    interaccion = request.json["interaccion"]
    consulta = """
        UPDATE Cubos SET nombre_cubo = %s, capacidad =%s, interaccion =%s,
            WHERE id = %s;
"""
    cur.execute(consulta, (nombre, capacidad, interaccion, id))
    mari.commit()
    cur.close()
    mari.close()

    return jsonify({"resultado" : "ok",
                    "id" : id})
#====================================================
#====================================================

@app.route("/api/estructura")
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

@app.route("/api/estructura/<int:id>", methods=('DELETE',))
def borrar_estructura(id):
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    cur.execute("DELETE FROM Estructura WHERE ID = %s", (id,))
    mari.commit()

    return jsonify({"resultado" : "ok",
                    "id" : id})

@app.route("/api/estructura/", methods=('POST',))
def agregar_estructura():
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    nombre = request.json["nombre"]
    consulta = """
        INSERT INTO Estructura (nombre_estructura, biomas_ID, dimension_ID) VALUES (%s, %s, %s)
"""

    cur.execute(consulta, (nombre, id))
    mari.commit()
    id = cur.lastrowid

    return jsonify({"resultado" : "ok",
                    "id" : id})

@app.route("/api/estructura/<int:id>", methods=('PUT',))
def modificar_estructura(id):
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    nombre = request.json["nombre"]
    consulta = """
        UPDATE Estructura SET nombre_estructura = %s, biomas_ID =%s, dimesion_ID =%s,
            WHERE id = %s;
"""
    cur.execute(consulta, (nombre, id))
    mari.commit()
    cur.close()
    mari.close()

    return jsonify({"resultado" : "ok",
                    "id" : id})
#====================================================
#====================================================

@app.route("/api/herramientas_basicas")
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

@app.route("/api/herramientas_basicas/<int:id>", methods=('DELETE',))
def borrar_herramientas(id):
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    cur.execute("DELETE FROM Herramientas_basicas WHERE ID = %s", (id,))
    mari.commit()

    return jsonify({"resultado" : "ok",
                    "id" : id})

@app.route("/api/herramientas_basicas/", methods=('POST',))
def agregar_herramientas():
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
    ataque = request.json["ataque"]
    consulta = """
        INSERT INTO Herramientas_basicas (nombre_herramienta, de_que_esta_hecho, durabilidad, ataque) VALUES (%s, %s, %s, %s)
"""

    cur.execute(consulta, (nombre, material, durabilidad, ataque, id))
    mari.commit()
    id = cur.lastrowid

    return jsonify({"resultado" : "ok",
                    "id" : id})

@app.route("/api/herramientas_basicas/<int:id>", methods=('PUT',))
def modificar_herrmientas(id):
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
    ataque = request.json["ataque"]
    consulta = """
        UPDATE Estructura SET nombre_herramienta = %s, de_que_esta_hecho =%s, durabilidad =%s,
        ataque =%s,  WHERE id = %s;
"""
    cur.execute(consulta, (nombre, material, durabilidad, ataque, id))
    mari.commit()
    cur.close()
    mari.close()

    return jsonify({"resultado" : "ok",
                    "id" : id})
#====================================================
#====================================================

@app.route("/api/jefes")
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

@app.route("/api/jefes/<int:id>", methods=('DELETE',))
def borrar_jefes(id):
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    cur.execute("DELETE FROM Jefes WHERE ID = %s", (id,))
    mari.commit()

    return jsonify({"resultado" : "ok",
                    "id" : id})

@app.route("/api/jefes/", methods=('POST',))
def agregar_jefes():
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    nombre = request.json["nombre"]
    salud = request.json["salud"]
    movilidad = request.json["movilidad"]
    invocacion = request.json["invocacion"]
    requisito_inv = request.json["requisitos_inv"]
    loot = request.json["loot"]
    loot_exp = request.json["loot_exp"]
    consulta = """
        INSERT INTO Jefes (nombre_jefe, salud, movilidad, puede_ser_invocado, requisito_invocacion, loot, loot_exp) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

    cur.execute(consulta, (nombre, salud, movilidad, invocacion, requisito_inv, loot, loot_exp, id))
    mari.commit()
    id = cur.lastrowid

    return jsonify({"resultado" : "ok",
                    "id" : id})

@app.route("/api/jefes/<int:id>", methods=('PUT',))
def modificar_jefes(id):
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    nombre = request.json["nombre"]
    salud = request.json["salud"]
    movilidad = request.json["movilidad"]
    invocacion = request.json["invocacion"]
    requisito_inv = request.json["requisitos_inv"]
    loot = request.json["loot"]
    loot_exp = request.json["loot_exp"]
    consulta = """
        UPDATE Jefes SET nombre_jefe = %s, salud =%s, movilidad =%s,
        puede_ser_invocado =%s, requisito_invocacion =%s, loot =%s,  loot_exp =%s  WHERE id = %s;
"""
    cur.execute(consulta, (nombre, salud, movilidad, invocacion, requisito_inv, loot, loot_exp, id))
    mari.commit()
    cur.close()
    mari.close()

    return jsonify({"resultado" : "ok",
                    "id" : id})
#====================================================
#====================================================

@app.route("/api/jefes_dimension")
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

@app.route("/api/jugador")
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

@app.route("/api/jugadores/<int:id>", methods=('DELETE',))
def borrar_jugadores(id):
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    cur.execute("DELETE FROM Jugadores WHERE ID = %s", (id,))
    mari.commit()

    return jsonify({"resultado" : "ok",
                    "id" : id})

@app.route("/api/jugadores/", methods=('POST',))
def agregar_jugadores():
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    nombre = request.json["nombre"]
    salud = request.json["salud"]
    ataque = request.json["ataque"]
    fecha_de_registro = request.json["fecha_de_registro"]
    consulta = """
        INSERT INTO Jugador (nombre_usuario, salud, ataque, fecha_de_registro) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

    cur.execute(consulta, (nombre, salud, ataque, fecha_de_registro, id))
    mari.commit()
    id = cur.lastrowid

    return jsonify({"resultado" : "ok",
                    "id" : id})

@app.route("/api/jugadores/<int:id>", methods=('PUT',))
def modificar_jugador(id):
    mari = mariadb.connect(
        user = "minecraft",
        password ="minecraft111",
        host ="10.9.120.5",
        database= "minecraft"
    )
    cur = mari.cursor(dictionary=True)
    nombre = request.json["nombre"]
    salud = request.json["salud"]
    ataque = request.json["ataque"]
    fecha_de_registro = request.json["fecha_de_registro"]
    consulta = """
        UPDATE Jugador SET nombre_jugador = %s, salud =%s, ataque =%s,
        puede_ser_invocado =%s, loot =%s, WHERE id = %s;
"""
    cur.execute(consulta, (nombre, salud, ataque, fecha_de_registro, id))
    mari.commit()
    cur.close()
    mari.close()

    return jsonify({"resultado" : "ok",
                    "id" : id})
#====================================================
#====================================================

@app.route("/api/zombie_salvador")
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