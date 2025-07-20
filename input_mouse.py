import objek2d
from objek2d import Objek2D
from renderer import display
from dragging import start_drag_object, stop_drag_object, do_drag_object, is_inside_object
from OpenGL.GLUT import *

# Fungsi konversi koordinat mouse ke koordinat OpenGL
def convert_mouse(x, y, window_height):
    return (x / glutGet(GLUT_WINDOW_WIDTH) * 2 - 1, ((window_height - y) / window_height) * 2 - 1)

# Fungsi klik mouse utama
def mouse_click(button, state, x, y):
    window_height = glutGet(GLUT_WINDOW_HEIGHT)
    pos = convert_mouse(x, y, window_height)

    # Seleksi objek jika mode seleksi aktif
    if objek2d.mode_seleksi and state == GLUT_DOWN:
        print("Posisi klik (OpenGL):", pos)
        for obj in objek2d.daftar_objek:
            if obj.jenis == 'point':
                px, py = obj.titik[0]
                print("Posisi objek:", px, py)
                print("Jarak X:", abs(pos[0] - px), "Jarak Y:", abs(pos[1] - py))
                if abs(pos[0] - px) < 0.2 and abs(pos[1] - py) < 0.3:  # Perbesar toleransi
                    objek2d.selected_objek = obj
                    objek2d.mode_seleksi = False
                    print("Objek terpilih!")
                    return
        print("Tidak ada objek yang dipilih.")
        return

    if state == GLUT_DOWN:
        if objek2d.selected_jenis == 'point':
            objek2d.daftar_objek.append(
                objek2d.Objek2D('point', [pos], objek2d.selected_warna, objek2d.line_thickness)
            )
        elif objek2d.selected_jenis in ['line', 'rect', 'ellipse']:
            objek2d.clicks.append(pos)
            if len(objek2d.clicks) == 2:
                objek2d.daftar_objek.append(
                    objek2d.Objek2D(objek2d.selected_jenis, objek2d.clicks.copy(), objek2d.selected_warna, objek2d.line_thickness)
                )
                objek2d.clicks.clear()

    elif state == GLUT_UP:  # mouse dilepas
        stop_drag_object()

# Fungsi passive motion (gerakan mouse saat drag)
def passive_motion(x, y):
    window_height = glutGet(GLUT_WINDOW_HEIGHT)
    pos = convert_mouse(x, y, window_height)
    do_drag_object(pos)

# Fungsi tambahan untuk mencetak klik mouse
def handle_mouse_click(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        print(f"Klik kiri di koordinat: ({x}, {y})")

# Fungsi gabungan untuk debugging klik dan interaksi
def mouse_combined(button, state, x, y):
    window_height = glutGet(GLUT_WINDOW_HEIGHT)  # Mengambil tinggi window secara dinamis
    pos = convert_mouse(x, y, window_height)
    if state == GLUT_DOWN:
        handle_mouse_click(button, state, x, y)
    elif state == GLUT_UP:
        stop_drag_object()

def motion(x, y):
    window_height = glutGet(GLUT_WINDOW_HEIGHT)
    pos = convert_mouse(x, y, window_height)
    do_drag_object(pos)