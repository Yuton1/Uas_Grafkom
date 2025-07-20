# main.py
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from renderer import display
from warna_dan_input import keyboard
from objek2d import reset_seleksi
from dragging import do_drag_object, stop_drag_object
from input_mouse import convert_mouse, mouse_click  # Import mouse_click
import objek2d

def mouse_combined(button, state, x, y):
    window_height = glutGet(GLUT_WINDOW_HEIGHT)  # Ambil tinggi window saat ini
    pos = convert_mouse(x, y, window_height)
    if state == GLUT_DOWN:
        handle_mouse_click(button, state, x, y)
    elif state == GLUT_UP:
        stop_drag_object()

def motion(x, y):
    window_height = glutGet(GLUT_WINDOW_HEIGHT)
    pos = convert_mouse(x, y, window_height)
    do_drag_object(pos)

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1, 1, -1, 1, -1, 1)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"2D Interactive Object Editor")
    init()
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutMouseFunc(mouse_click)  # Ganti dari mouse_combined ke mouse_click
    glutMotionFunc(motion)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()

def handle_mouse_click(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        window_height = glutGet(GLUT_WINDOW_HEIGHT)
        pos = convert_mouse(x, y, window_height)
        print("Posisi klik (OpenGL):", pos)

        # Seleksi objek dari daftar_objek
        for obj in objek2d.daftar_objek:
            if hasattr(obj, "titik"):
                px, py = obj.titik[0]
                print("Posisi objek:", px, py)
                print("Jarak X:", abs(pos[0] - px), "Jarak Y:", abs(pos[1] - py))
                if abs(pos[0] - px) < 0.3 and abs(pos[1] - py) < 0.3:
                    objek2d.selected_objek = obj
                    objek2d.mode_seleksi = False
                    print("Objek terpilih!")
                    return

        print("Tidak ada objek yang dipilih.")
