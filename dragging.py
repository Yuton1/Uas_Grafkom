# dragging.py

dragging_obj = False
drag_start = (0, 0)

def is_inside_object(pos, obj):
    if obj.jenis in ['rect', 'ellipse', 'line']:
        x1, y1 = obj.titik[0]
        x2, y2 = obj.titik[1]
        xmin, xmax = min(x1, x2), max(x1, x2)
        ymin, ymax = min(y1, y2), max(y1, y2)
        return xmin <= pos[0] <= xmax and ymin <= pos[1] <= ymax
    elif obj.jenis == 'point':
        x, y = obj.titik[0]
        return abs(pos[0] - x) < 0.05 and abs(pos[1] - y) < 0.05
    return False

def start_drag_object(pos, obj):
    global dragging_obj, drag_start
    dragging_obj = True
    drag_start = pos

def stop_drag_object():
    global dragging_obj
    dragging_obj = False

def do_drag_object(pos):
    from objek2d import selected_objek
    global dragging_obj, drag_start
    if dragging_obj and selected_objek:
        dx = pos[0] - drag_start[0]
        dy = pos[1] - drag_start[1]
        selected_objek.transform['tx'] += dx
        selected_objek.transform['ty'] += dy
        drag_start = pos
