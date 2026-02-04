import pgzrun
WIDTH= 450
HEIGHT= 450
def draw():
    screen.fill("#000000")
    w = 450
    h = 125
    for i in range(27):
        r = Rect((225,225),(w,h))
        r.center=(225,225)
        screen.draw.rect(r, "#FFFFFF")
        w = w-12.5
        h = h+12.5
    
pgzrun.go()