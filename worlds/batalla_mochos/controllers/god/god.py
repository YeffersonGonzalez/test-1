#Batalla de mochos

from controller import Supervisor
import math

supervisor = Supervisor()
timestep = int(supervisor.getBasicTimeStep())

# Nodos Robots por DEF name
robot1 = supervisor.getFromDef("robot")
robot2 = supervisor.getFromDef("robot2")
arena = supervisor.getFromDef("arena")

arena_center = [0.0, 0.0, 0.0]

if robot1 is None or robot2 is None:
    print("No se encontró alguno de los robots")
    exit()

def robot_caido(robot):
    #Agregar aquí una lógica para evaluar si un mocho está caido
    pass

# Esta función resetea la posición y la orientación de un robot
def levantar_robot(robot):
    nueva_posicion = [0.0, 0.0, 0.2]
    t = robot.getField("translation")
    t.setSFVec3f(nueva_posicion)
    
    nueva_orientacion = [1, 0, 0, 0]    
    r = robot.getField("rotation")
    r.setSFRotation(nueva_orientacion)
    
reset_times = {'robot1': timestep*80/100, 'robot2': timestep*100/100}

while (supervisor.step(timestep) !=-1):  
    #print(supervisor.getTime())
    rotacion1 = robot1.getField("rotation").getSFVec3f() 
    rotacion2 = robot2.getField("rotation").getSFVec3f() 
    print(rotacion1[3])
    
    
    if rotacion1[3]  :
        levantar_robot(robot1)
    if (supervisor.getTime() % reset_times['robot2']) == 0:
        levantar_robot(robot2)
        
    diametro_arena = arena.getField("floorTileSize").getSFFloat()[0]
    p_robot1 = robot1.getField("translation").getSFVec3f()   
    p_robot2 = robot2.getField("translation").getSFVec3f()  
    
    if math.sqrt(p_robot1[0] ** 2 + p_robot1[1] ** 2 + p_robot1[2] ** 2) > 2*diametro_arena:
       print('robot1 perdió')
       exit()
    if math.sqrt(p_robot2[0] ** 2 + p_robot2[1] ** 2 + p_robot2[2] ** 2) > 2*diametro_arena:
       print('robot2 perdió')
       exit()