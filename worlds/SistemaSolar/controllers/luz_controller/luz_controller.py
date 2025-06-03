from controller import Supervisor
import math

robot = Supervisor()
timestep = int(robot.getBasicTimeStep())

sol = robot.getFromDef("sol")
luz = robot.getFromDef("luz_sol")

while robot.step(timestep) != -1:
    # Obtener posición del sol
    pos_sol = sol.getField("translation").getSFVec3f()

    # Queremos que la luz apunte desde el Sol hacia el centro del sistema (0,0,0)
    direccion = [-pos_sol[0], -pos_sol[1], -pos_sol[2]]

    # Normalizar dirección
    magnitud = math.sqrt(sum(x**2 for x in direccion))
    if magnitud != 0:
        direccion = [x / magnitud for x in direccion]
        luz.getField("direction").setSFVec3f(direccion)