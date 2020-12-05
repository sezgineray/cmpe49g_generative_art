t=0

def setup():
    size(800, 800)
    background(0)
    t=0

def draw():
    global t
    
    m = noise(t)
    x = map(m,0,1,0,width)
    n = noise(t+55)
    y = map(n,0,1,0,height)
    
    r = noise(t+100)
    rr = map(r,0,1,2,5)
    
    cr = noise(t+2)
    cg = noise(t+100)
    cb = noise(t+222)
    
    ccr = map(cr,0,1,0,255)
    ccg = map(cg,0,1,0,255)
    ccb = map(cb,0,1,0,255)
    strokeWeight(rr)
    stroke(ccr,ccg,ccb)
    
    line(width/2, height/2, x, y)
    
    t += 0.01
