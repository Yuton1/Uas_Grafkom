# kontrol.py

rot_x = 0
rot_y = 0

def keyboard(key, x, y):
    global rot_x, rot_y
    key = key.decode('utf-8')

    if key == 'w':
        rot_x -= 5
    elif key == 's':
        rot_x += 5
    elif key == 'a':
        rot_y -= 5
    elif key == 'd':
        rot_y += 5
    elif key == 'r':
        rot_x = 0
        rot_y = 0

def update_transform():
    return rot_x, rot_y
