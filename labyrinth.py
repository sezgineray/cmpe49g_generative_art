H, W = 800, 800

step = 40

def setup():
    global W, H
    size(W, H)
    background(150, 0, 150)
    strokeWeight(3)
    stroke(0,0,100)
    noLoop()


def draw():
    background(150, 0, 150)
    global step
    for x in range(0,W,step): 
        for y in range(0,H,step):
            strokeWeight(noise(x,y)*20)
            if random(1) > .5:
                line(x,y,x+step, y+step) 
            else:
                line(x+step,y,x, y+step) 
