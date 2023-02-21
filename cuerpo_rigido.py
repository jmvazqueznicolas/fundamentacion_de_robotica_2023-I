"""
Robotics Fundamentals
Tec de Monterrey CCM

Prerequisites
    1.- Install Conda and create an environment (Python>=3.7).
        e.g. "conda create -n robotica python=3.7"
    2.- Activate the enviroment previously created.
        e.g. "conda activate robotica"
    3.- Install roboticstoolbox and sympy libraries.
        e.g. "pip install roboticstoolbox-python"
             "pip install sympy"
"""

# Importing Libraries
from spatialmath.base import rot2
from sympy import simplify, Matrix
import spatialmath.base as base
import numpy as np

# 2D Case
# Numeric
R = rot2(0.2) # Radians
det = np.linalg.det(R)
print("La matriz es\n", R)
print("y su determinante es", det)
det_RxR = np.linalg.det(np.matmul(R, R)) 
print("El determinante de R*R es", det_RxR)

# Symbolic
theta = base.sym.symbol('\u03B8')  # theta = \u03B8
rot_sym = base.rot2(theta)
print("La matriz de rotacion (simbólica) es: ")
print(rot_sym)
RxR_sym = rot_sym.dot(rot_sym)
print(RxR_sym)
print(simplify(RxR_sym))
RxR_sym = Matrix(RxR_sym)
print(simplify(RxR_sym.det()))

#3D Case