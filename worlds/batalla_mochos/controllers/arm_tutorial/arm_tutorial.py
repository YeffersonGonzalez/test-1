from controller import Robot

robot=Robot()
timestep=64

m=robot.getDevice("motor")
m.setPosition(float('inf'))
m.setVelocity(0.0)

pSensor=robot.getDevice("ps")
pSensor.enable(timestep)

speed=3
k=0

while (robot.step(timestep) !=-1):
    m.setVelocity(speed)
    k=pSensor.getValue()
    