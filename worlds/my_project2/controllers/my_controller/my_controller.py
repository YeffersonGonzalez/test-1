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

# Obtener nodos
sol = robot.getFromDef("sol")
mercurio = robot.getFromDef("mercurio")
venus = robot.getFromDef("venus")
tierra = robot.getFromDef("tierra")
marte = robot.getFromDef("marte")
jupiter = robot.getFromDef("jupiter")
saturno = robot.getFromDef("saturno")
urano = robot.getFromDef("urano")
neptuno = robot.getFromDef("neptuno")
pluton = robot.getFromDef("pluton")

# Constantes
#radius_orbit = 0.6   # radio de la órbita de 2 alrededor de 1
#angular_speed = 0.5  # radianes por segundo

# Loop principal
while robot.step(timestep) != -1:
    t = robot.getTime()  # tiempo actual en segundos

    # 1. Obtener posición fija de caja 1
    trans_a = np.array(sol.getField("translation").getSFVec3f())
    H_wa = homogeneous_matrix(np.eye(3), trans_a)

    # 2. Rotación incremental
    theta = 1.6 * t
    R = rotation_matrix_y(theta)

    # 3. Posición relativa de 2 respecto a 1 (en el eje X)
    t_ab = np.array([0.4, 0, 0])
    H_ab = homogeneous_matrix(R, R @ t_ab)

    # 4. Transformar a coordenadas globales
    H_wb = H_wa @ H_ab
    pos_b = H_wb[:3, 3]

    # Mercurio
    mercurio.getField("translation").setSFVec3f(pos_b.tolist())

    # Venus
    theta = 1.2 * t
    R = rotation_matrix_y(theta)
    t_ab = np.array([0.7, 0, 0])
    H_ab = homogeneous_matrix(R, R @ t_ab)
    H_wb = H_wa @ H_ab
    pos_b = H_wb[:3, 3]
    venus.getField("translation").setSFVec3f(pos_b.tolist())

    # Tierra
    theta = 1.0 * t
    R = rotation_matrix_y(theta)
    t_ab = np.array([1.0, 0, 0])
    H_ab = homogeneous_matrix(R, R @ t_ab)
    H_wb = H_wa @ H_ab
    pos_b = H_wb[:3, 3]
    tierra.getField("translation").setSFVec3f(pos_b.tolist())

    # Marte
    theta = 0.8 * t
    R = rotation_matrix_y(theta)
    t_ab = np.array([1.5, 0, 0])
    H_ab = homogeneous_matrix(R, R @ t_ab)
    H_wb = H_wa @ H_ab
    pos_b = H_wb[:3, 3]
    marte.getField("translation").setSFVec3f(pos_b.tolist())

    # Júpiter
    theta = 0.5 * t
    R = rotation_matrix_y(theta)
    t_ab = np.array([2.2, 0, 0])
    H_ab = homogeneous_matrix(R, R @ t_ab)
    H_wb = H_wa @ H_ab
    pos_b = H_wb[:3, 3]
    jupiter.getField("translation").setSFVec3f(pos_b.tolist())

    # Saturno
    theta = 0.3 * t
    R = rotation_matrix_y(theta)
    t_ab = np.array([2.8, 0, 0])
    H_ab = homogeneous_matrix(R, R @ t_ab)
    H_wb = H_wa @ H_ab
    pos_b = H_wb[:3, 3]
    saturno.getField("translation").setSFVec3f(pos_b.tolist())

    # Urano
    theta = 0.2 * t
    R = rotation_matrix_y(theta)
    t_ab = np.array([3.5, 0, 0])
    H_ab = homogeneous_matrix(R, R @ t_ab)
    H_wb = H_wa @ H_ab
    pos_b = H_wb[:3, 3]
    urano.getField("translation").setSFVec3f(pos_b.tolist())

    # Neptuno
    theta = 0.15 * t
    R = rotation_matrix_y(theta)
    t_ab = np.array([4.0, 0, 0])
    H_ab = homogeneous_matrix(R, R @ t_ab)
    H_wb = H_wa @ H_ab
    pos_b = H_wb[:3, 3]
    neptuno.getField("translation").setSFVec3f(pos_b.tolist())

    # Plutón
    theta = 0.1 * t
    R = rotation_matrix_y(theta)
    t_ab = np.array([4.5, 0, 0])
    H_ab = homogeneous_matrix(R, R @ t_ab)
    H_wb = H_wa @ H_ab
    pos_b = H_wb[:3, 3]
    pluton.getField("translation").setSFVec3f(pos_b.tolist())