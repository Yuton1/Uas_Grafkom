#objek2d.py
from OpenGL.GL import *
from math import cos, sin

class Objek2D:
    def __init__(self, jenis, titik, warna, ketebalan):
        self.jenis = jenis
        self.titik = titik
        self.warna = warna
        self.ketebalan = ketebalan
        self.transform = {'tx': 0, 'ty': 0, 'rot': 0, 'scale': 1}

    def draw(self):
        glColor3fv(self.warna)
        glLineWidth(self.ketebalan)
        if self.jenis == 'point':
            glBegin(GL_POINTS)
            glVertex2fv(self.titik[0])
            glEnd()
        elif self.jenis == 'line':
            glBegin(GL_LINES)
            glVertex2fv(self.titik[0])
            glVertex2fv(self.titik[1])
            glEnd()
        elif self.jenis == 'rect':
            glBegin(GL_LINE_LOOP)
            glVertex2fv(self.titik[0])
            glVertex2f(self.titik[1][0], self.titik[0][1])
            glVertex2fv(self.titik[1])
            glVertex2f(self.titik[0][0], self.titik[1][1])
            glEnd()
        elif self.jenis == 'ellipse':
            cx, cy = self.titik[0]
            rx = abs(self.titik[1][0] - self.titik[0][0])
            ry = abs(self.titik[1][1] - self.titik[0][1])
            glBegin(GL_LINE_LOOP)
            for i in range(100):
                theta = 2.0 * 3.1415926 * i / 100
                x = rx * cos(theta)
                y = ry * sin(theta)
                glVertex2f(cx + x, cy + y)
            glEnd()

daftar_objek = []
clicks = []
selected_jenis = 'point'
daftar_warna = [
    (1.0, 0.0, 0.0),  # Merah
    (0.0, 1.0, 0.0),  # Hijau
    (0.0, 0.0, 1.0),  # Biru
]
selected_warna = daftar_warna[0]
line_thickness = 2
window_area = []
selected_objek = None
mode_seleksi = False

def reset_seleksi():
    global selected_objek
    selected_objek = None
