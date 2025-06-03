from controller import Supervisor
import math
import random

supervisor = Supervisor()
timestep = int(supervisor.getBasicTimeStep())

root = supervisor.getRoot()
anillo_saturno = root.getField("children")

def generar_asteroides_en_anillo(cantidad, centro, radio_interno, radio_externo, altura=0.0):
    for i in range(cantidad):
        angulo = random.uniform(0, 2 * math.pi)
        radio = random.uniform(radio_interno, radio_externo)
        x = centro[0] + radio * math.cos(angulo)
        z = centro[2] + radio * math.sin(angulo)
        y = centro[1] + random.uniform(-0.01, 0.01)  # pequeño grosor vertical

        nodo_asteroide = f"""
        Solid {{
          translation {x} {y} {z}
          name "asteroide_{i}"
          children [
            Shape {{
              appearance Appearance {{
                material Material {{
                  diffuseColor 0.4 0.4 0.4
                }}
              }}
              geometry Sphere {{
                radius 0.01
              }}
            }}
          ]
          physics Physics {{
            mass 0.001
          }}
        }}
        """
        anillo_saturno.importMFNodeFromString(-1, nodo_asteroide)

# Espera un poco antes de insertar
supervisor.step(timestep * 5)

# Generar asteroides alrededor de Saturno, por ejemplo
generar_asteroides_en_anillo(
    cantidad=100,
    centro=[5, 0, 0],  # posición de Saturno
    radio_interno=0.5,
    radio_externo=0.7
)

# Loop normal de simulación
while supervisor.step(timestep) != -1:
    pass
