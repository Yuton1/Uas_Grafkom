from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import glutSwapBuffers
from objek3d import draw_kubus
from kontrol import update_transform

def render_scene():
    """Fungsi untuk menggambar dan me-render seluruh scene 3D"""
    rot_x, rot_y = update_transform()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Kamera
    gluLookAt(5, 5, 5,   0, 0, 0,   0, 1, 0)

    # Transformasi (rotasi)
    glRotatef(rot_x, 1, 0, 0)
    glRotatef(rot_y, 0, 1, 0)

    # Warna objek
    glColor3f(0.4, 0.7, 1.0)

    draw_kubus()

    glutSwapBuffers()
