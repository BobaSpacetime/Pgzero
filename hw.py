import pgzrun
WIDTH= 680
HEIGHT= 450
def draw():
    screen.fill("#0D0028")
    r = Rect((440,325),(200,100))
    screen.draw.rect(r,"#A8DEFF")
    rr = Rect((40,325),(200,100))
    screen.draw.filled_rect(rr,"#DDB5FD")
    screen.draw.filled_circle((140,125), 100, "#B87EFF")
    screen.draw.circle((540,125), 100, "#9EAEFF")


pgzrun.go()
