import pgzrun
import random 

WIDTH = 450
HEIGHT = 450

a = Actor("alien")
a.x = 225
a.y = 225
msg = "Press the alien."
def draw():
    screen.fill("Black")
    a.draw()  
    screen.draw.text(msg, (255,10), color = "#CBC5FF")  

def on_mouse_down(pos): 
    global msg
    if a.collidepoint(pos):
        a.x = random.randint(1,449)
        a.y = random.randint(1,449)
        msg = "Good shot"
    else:
        msg = "SUCKER"


pgzrun.go()