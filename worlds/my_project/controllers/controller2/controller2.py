"""
Ejemplo  de un controlador de un robot tipo supervisor

2 esferas ball1 y ball2. ball2 hace seguimiento de la posición de ball1
"""

from controller import Supervisor
import numpy as np

supervisor = Supervisor()
timestep = int(supervisor.getBasicTimeStep())

ball1 = supervisor.getFromDef("ball1")
ball2 = supervisor.getFromDef("ball2")

translation_field = ball2.getField("translation")

children1 = ball1.getField("children")
shape1 = children1.getMFNode(0)
geometry1 = shape1.getField("geometry")
sphere1 = geometry1.getSFNode()
radio_field1 = sphere1.getField("radius")
radio1 = radio_field1.getSFFloat()

#print(radio1)

children2 = ball2.getField("children")
shape2 = children2.getMFNode(0)
geometry2 = shape2.getField("geometry")
sphere2 = geometry2.getSFNode()
radio_field2 = sphere2.getField("radius")
radio2 = radio_field2.getSFFloat()

#print(radio2)

def get_position(node):
    return np.array(node.getField("translation").getSFVec3f())

speed = 0.01  # Velocidad constante

while supervisor.step(timestep) != -1:
    pos1 = get_position(ball1)
    pos2 = get_position(ball2)
    
    direction = pos1 - pos2
    distance = np.linalg.norm(direction)
    

    if distance > (radio1 + radio2):
        direction_normalized = direction / distance
        new_pos = pos2 + direction_normalized * speed
        # Mantener altura Y
        #new_pos[1] = pos2[1]
        #print(new_pos)

        translation_field.setSFVec3f(new_pos.tolist())
        
   # if np.linalg.norm(pos1 - new_pos) < (radio1 + radio2):
       # direction_normalized = direction / distance
       # new_pos = pos1 - direction_normalized * speed
        
       # translation_field.setSFVec3f(new_pos.tolist())