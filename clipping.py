# clipping.py
from objek2d import window_area
from OpenGL.GL import *
from OpenGL.GLUT import glutSwapBuffers

INSIDE, LEFT, RIGHT, BOTTOM, TOP = 0, 1, 2, 4, 8
dragging = False
drag_offset = (0, 0)

def compute_outcode(x, y, xmin, xmax, ymin, ymax):
    code = INSIDE
    if x < xmin: code |= LEFT
    elif x > xmax: code |= RIGHT
    if y < ymin: code |= BOTTOM
    elif y > ymax: code |= TOP
    return code

def cohen_sutherland_clip(x1, y1, x2, y2, xmin, xmax, ymin, ymax):
    outcode1 = compute_outcode(x1, y1, xmin, xmax, ymin, ymax)
    outcode2 = compute_outcode(x2, y2, xmin, xmax, ymin, ymax)

    while True:
        if not (outcode1 | outcode2):
            return True, x1, y1, x2, y2
        elif outcode1 & outcode2:
            return False, None, None, None, None
        else:
            x, y = 0, 0
            outcode_out = outcode1 if outcode1 else outcode2
            if outcode_out & TOP:
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif outcode_out & BOTTOM:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif outcode_out & RIGHT:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif outcode_out & LEFT:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin
            if outcode_out == outcode1:
                x1, y1 = x, y
                outcode1 = compute_outcode(x1, y1, xmin, xmax, ymin, ymax)
            else:
                x2, y2 = x, y
                outcode2 = compute_outcode(x2, y2, xmin, xmax, ymin, ymax)

def draw_window_box():
    if len(window_area) == 2:
        x1, y1 = window_area[0]
        x2, y2 = window_area[1]

        # Gambar kotak hijau sebagai area clipping
        glColor3f(0, 1, 0)
        glLineWidth(1)
        glBegin(GL_LINE_LOOP)
        glVertex2f(x1, y1)
        glVertex2f(x2, y1)
        glVertex2f(x2, y2)
        glVertex2f(x1, y2)
        glEnd()

def start_drag(pos):
    global dragging, drag_offset
    if len(window_area) == 2:
        x1, y1 = window_area[0]
        x2, y2 = window_area[1]
        if x1 <= pos[0] <= x2 and y1 <= pos[1] <= y2:
            dragging = True
            drag_offset = pos[0] - x1, pos[1] - y1

def stop_drag():
    global dragging
    dragging = False

def do_drag(pos):
    global dragging
    if dragging and len(window_area) == 2:
        dx, dy = drag_offset
        w = window_area[1][0] - window_area[0][0]
        h = window_area[1][1] - window_area[0][1]
        x1, y1 = pos[0] - dx, pos[1] - dy
        x2, y2 = x1 + w, y1 + h
        window_area[0] = (x1, y1)
        window_area[1] = (x2, y2)
