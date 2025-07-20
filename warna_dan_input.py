#warna_dan_input.py
import objek2d

def keyboard(key, x, y):
    # Pilihan warna
    if key == b'1':
        objek2d.selected_warna = objek2d.daftar_warna[0]
    elif key == b'2':
        objek2d.selected_warna = objek2d.daftar_warna[1]
    elif key == b'3':
        objek2d.selected_warna = objek2d.daftar_warna[2]
    # Ketebalan garis
    elif key == b'+':
        objek2d.line_thickness += 1
    elif key == b'-':
        objek2d.line_thickness = max(1, objek2d.line_thickness - 1)
    # Pilih jenis objek
    elif key == b'p':
        objek2d.selected_jenis = 'point'
    elif key == b'l':
        objek2d.selected_jenis = 'line'
    elif key == b'r':
        objek2d.selected_jenis = 'rect'
    elif key == b'e':
        objek2d.selected_jenis = 'ellipse'
    elif key == b'q':
        objek2d.mode_seleksi = True
        print("mode seleksi:", objek2d.mode_seleksi)
