t=0

def setup():
    size(800, 800)
    stroke(255)
    background(100)
    t=0

def draw():
    global t
    # background(100)
    m = noise(t)
    x = map(m,0,1,0,width)
    n = noise(t+2)
    y = map(n,0,1,0,height)
    
    r = noise(t+100)
    rr = map(r,0,1,20,120)
    
    cr = noise(t+2)
    cg = noise(t+22)
    cb = noise(t+222)
    
    ccr = map(cr,0,1,0,255)
    ccg = map(cg,0,1,0,255)
    ccb = map(cb,0,1,0,255)
    fill(ccr,ccg,ccb)
    ellipse(x,y,rr,rr)
    t += 0.01
