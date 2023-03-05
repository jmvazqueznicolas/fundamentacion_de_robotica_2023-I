# Importing Libraries
import roboticstoolbox as rtb
import math

# Joint angles (rad)
pi = math.pi
q = [pi/4 , 0.2, pi, 0.3, -pi/6 , -1.3, 0.4]
#q = [pi/6, 0.8, 0.1, 0.2, 0.4, 0.5, 0.4]
    
# RR planar robot from library
robot1 = rtb.models.DH.Baxter()
print(robot1)
T = robot1.fkine(q)
print(T)
robot1.plot(q, block=True)