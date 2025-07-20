from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from lighting import setup_lighting
from kontrol import keyboard, update_transform
from renderer3d import render_scene

def display():
    render_scene()

def idle():
    glutPostRedisplay()

def init():
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    setup_lighting()
    glClearColor(0.9, 0.9, 0.9, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 800/600, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Modul B - Kubus 3D")
    init()
    glutDisplayFunc(display)
    glutIdleFunc(idle)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

main()
