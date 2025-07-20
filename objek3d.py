from OpenGL.GL import *

def draw_kubus():
    vertices = [
        [-1, -1, -1],  # 0
        [ 1, -1, -1],  # 1
        [ 1,  1, -1],  # 2
        [-1,  1, -1],  # 3
        [-1, -1,  1],  # 4
        [ 1, -1,  1],  # 5
        [ 1,  1,  1],  # 6
        [-1,  1,  1],  # 7
    ]

    faces = [
        [0, 1, 2, 3],  # Belakang
        [4, 5, 6, 7],  # Depan
        [0, 4, 7, 3],  # Kiri
        [1, 5, 6, 2],  # Kanan
        [3, 2, 6, 7],  # Atas
        [0, 1, 5, 4],  # Bawah
    ]

    normals = [
        [ 0,  0, -1],  # belakang
        [ 0,  0,  1],  # depan
        [-1,  0,  0],  # kiri
        [ 1,  0,  0],  # kanan
        [ 0,  1,  0],  # atas
        [ 0, -1,  0],  # bawah
    ]

    glBegin(GL_QUADS)
    for i in range(6):
        glNormal3fv(normals[i])  # pencahayaan
        for j in faces[i]:
            glVertex3fv(vertices[j])
    glEnd()
