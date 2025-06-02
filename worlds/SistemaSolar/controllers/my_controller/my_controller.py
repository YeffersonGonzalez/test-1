from controller import Supervisor
import numpy as np

def rotation_matrix_y(theta):
    """Rotación 3x3 sobre eje Y"""
    c = np.cos(theta)
    s = np.sin(theta)
    return np.array([
        [ c, -s, 0],
        [ s,  c, 0],
        [ 0,  0, 1]
    ])

def homogeneous_matrix(R, t):
    """Devuelve matriz homogénea 4x4"""
    H = np.eye(4)
    H[:3, :3] = R
    H[:3, 3] = t
    return H

# Iniciar supervisor
robot = Supervisor()
timestep = int(robot.getBasicTimeStep())

#Diccionario de planetas con: (nodo, semieje mayor a, semieje menor b, velocidad órbita, velocidad rotación)
planetas = {
    "mercurio":  (robot.getFromDef("mercurio"), 0.40, 0.38, 1.6, 0.017),
    "venus":     (robot.getFromDef("venus"),    0.70, 0.69, 1.2, -0.004),
    "tierra":    (robot.getFromDef("tierra"),   1.00, 0.98, 1.0, 0.26),
    "marte":     (robot.getFromDef("marte"),    1.50, 1.47, 0.8, 0.24),
    "jupiter":   (robot.getFromDef("jupiter"),  2.20, 2.15, 0.5, 2.0),
    "saturno":   (robot.getFromDef("saturno"),  2.80, 2.72, 0.3, 1.7),
    "urano":     (robot.getFromDef("urano"),    3.50, 3.40, 0.2, 1.3),
    "neptuno":   (robot.getFromDef("neptuno"),  4.00, 3.90, 0.15, 1.2),
    "pluton":    (robot.getFromDef("pluton"),   4.50, 4.25, 0.1, 0.07)
}

# Diccionario de lunas con: (nodo,  radio, velocidad órbita, velocidad rotación)
lunas = {
    # Lunas de Marte
    "fobos": (robot.getFromDef("fobos"), 0.05, 4.8, 0.3),
    "deimos": (robot.getFromDef("deimos"), 0.08, 2.7, 0.25),

    # Lunas de Júpiter
    "io": (robot.getFromDef("io"), 0.12, 1.77, 0.6),
    "europa": (robot.getFromDef("europa"), 0.16, 1.3, 0.5),
    "ganimedes": (robot.getFromDef("ganimedes"), 0.20, 1.0, 0.4),
    "calisto": (robot.getFromDef("calisto"), 0.24, 0.75, 0.35),

    # Lunas de Saturno
    "titán": (robot.getFromDef("titan"), 0.25, 0.6, 0.3),
    "encélado": (robot.getFromDef("encelado"), 0.20, 1.1, 0.25),

    # Luna de la Tierra
    "luna_tierra": (robot.getFromDef("luna"), 0.1, 2.0, 0.5),

    # Lunas de Urano
    "titania": (robot.getFromDef("titania"), 0.15, 1.6, 0.3),
    "oberon": (robot.getFromDef("oberon"), 0.18, 1.2, 0.3),

    # Luna de Neptuno
    "triton": (robot.getFromDef("triton"), 0.14, 1.4, 0.3),

    # Luna de Plutón
    "caronte": (robot.getFromDef("caronte"), 0.07, 2.2, 0.2),
}



# Constantes
#radius_orbit = 0.6   # radio de la órbita de 2 alrededor de 1
#angular_speed = 0.5  # radianes por segundo

# Loop principal
while robot.step(timestep) != -1:
    t = robot.getTime()

    # Obtener posición del sol
    sol = robot.getFromDef("sol")
    sol_position = np.array(sol.getField("translation").getSFVec3f())
    H_wa = homogeneous_matrix(np.eye(3), sol_position)

    for nombre, (nodo, a, b, velocidad, v_rotacion) in planetas.items():
        theta = velocidad * t
        x = a * np.cos(theta)
        z = b * np.sin(theta)
        pos = np.array([x, 0, z])
        pos_global = sol_position + pos
        nodo.getField("translation").setSFVec3f(pos_global.tolist())

        angulo_giro = v_rotacion * t
        nodo.getField("rotation").setSFRotation([0, 1, 0, angulo_giro])

    # Obtener posición de la tierra
    pos_planetas = {
    "marte": np.array(robot.getFromDef("marte").getField("translation").getSFVec3f()),
    "jupiter": np.array(robot.getFromDef("jupiter").getField("translation").getSFVec3f()),
    "saturno": np.array(robot.getFromDef("saturno").getField("translation").getSFVec3f()),
    "tierra": np.array(robot.getFromDef("tierra").getField("translation").getSFVec3f()),
    "urano": np.array(robot.getFromDef("urano").getField("translation").getSFVec3f()),
    "neptuno": np.array(robot.getFromDef("neptuno").getField("translation").getSFVec3f()),
    "pluton": np.array(robot.getFromDef("pluton").getField("translation").getSFVec3f()),
    }

    for nombre, (nodo, radio, velocidad, v_rotacion) in lunas.items():
        if nombre in ["fobos", "deimos"]:
            planeta_pos = pos_planetas["marte"]
        elif nombre in ["io", "europa", "ganimedes", "calisto"]:
            planeta_pos = pos_planetas["jupiter"]
        elif nombre in ["titán", "encélado"]:
            planeta_pos = pos_planetas["saturno"]
        elif nombre == "luna_tierra":
            planeta_pos = pos_planetas["tierra"]
        elif nombre in ["titania", "oberon"]:
            planeta_pos = pos_planetas["urano"]
        elif nombre == "triton":
            planeta_pos = pos_planetas["neptuno"]
        elif nombre == "caronte":
            planeta_pos = pos_planetas["pluton"]
        else:
            np.array([0, 0, 0])

        theta = velocidad * t
        x = radio * np.cos(theta)
        z = radio * np.sin(theta)
        pos_local = np.array([x, 0, z])
        pos_global = planeta_pos + pos_local
        nodo.getField("translation").setSFVec3f(pos_global.tolist())

        angulo_giro = v_rotacion * t
        nodo.getField("rotation").setSFRotation([0, 1, 0, angulo_giro])