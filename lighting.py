from OpenGL.GL import *

def setup_lighting():
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    
    # Light Source (posisi dan properti)
    light_pos = [5.0, 5.0, 5.0, 1.0]
    ambient = [0.2, 0.2, 0.2, 1.0]
    diffuse = [0.7, 0.7, 0.7, 1.0]
    specular = [1.0, 1.0, 1.0, 1.0]

    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, specular)

    # Material objek
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    glMateriali(GL_FRONT, GL_SHININESS, 50)
