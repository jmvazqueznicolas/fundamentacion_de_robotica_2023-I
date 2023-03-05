# If a ffmpeg releated error occurs run:
# sudo apt install ffmpeg

# Importing Libraries
from roboticstoolbox import ET2, ET
import roboticstoolbox as rtb
import math

# Joint angles (rad)
pi = math.pi
q = [pi/6, 0.8]
a1 = 0.5
a2 = 1 

# 2D
T_01 = ET2.R(q[0], 'rad') * ET2.tx(a1)
T_12 = ET2.R(q[1], 'rad') * ET2.tx(a2)
T_02 = T_01 * T_12
K_2d = T_02.fkine([])
print("2-DOF planar robot (2D space) - FK")
print(K_2d)

# 3D
T_01_3d = ET.Rz(q[0], 'rad') * ET.tx(a1)
T_12_3d = ET.Rz(q[1], 'rad') * ET.tx(a2)
T_02_3d = T_01_3d * T_12_3d
K_3d = T_02_3d.fkine([])
print("2-DOF planar robot (3D space)- FK")
print(K_3d)

# RR planar robot from library
robot1 = rtb.models.ETS.Planar2()
T = robot1.fkine(q)
print("2-DOF planar robot (library) - FK")
print(T)
robot1.plot(q, block=True)


#robot1.plot([pi/6, 0.8], movie='2D_sim.gif')

"""
print(type(T_01_K))
# Método 2
T1 = transl2(1, 2) #trot2(30, 'deg') #
print(T1)

# Graficar movimiento
#tranimate(transl(1,0,0)@trotz(1), frame='A', arrow=False, dims=[0, 2], movie='spin.mp4')

R = rotx(pi/2)
tranimate(R, movie='rot.mp4')
"""