from OpenGL.GL import *
from OpenGL.GLUT import *
import objek2d

def draw_object(obj):
    glPushMatrix()
    apply_transform(obj)
    draw_shape(obj.shape)
    glPopMatrix()

def apply_transform(obj):
    glLoadIdentity() 
    glTranslatef(obj.transform['tx'], obj.transform['ty'], 0)
    glRotatef(obj.transform['rot'], 0, 0, 1)
    glScalef(obj.transform['scale'], obj.transform['scale'], 1)

def draw_shape(shape):
    glColor3f(*shape['color'])

    if shape['type'] == 'triangle':
        glBegin(GL_TRIANGLES)
        for vertex in shape['vertices']:
            glVertex2f(*vertex)
        glEnd()

    elif shape['type'] == 'quad':
        glBegin(GL_QUADS)
        for vertex in shape['vertices']:
            glVertex2f(*vertex)
        glEnd()

    elif shape['type'] == 'polygon':
        glBegin(GL_POLYGON)
        for vertex in shape['vertices']:
            glVertex2f(*vertex)
        glEnd()
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    # Gambar semua objek yang ada di daftar_objek
    for obj in objek2d.daftar_objek:
        obj.draw()
    glutSwapBuffers()