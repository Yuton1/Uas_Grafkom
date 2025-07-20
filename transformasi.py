#transformasi.py
from OpenGL.GL import *

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Latar belakang putih
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1, 1, -1, 1, -1, 1)  # Koordinat ortogonal
    glMatrixMode(GL_MODELVIEW)
