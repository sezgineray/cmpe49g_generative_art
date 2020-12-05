class Stick():
    x = 0
    y = 0
    rcolor = 0
    gcolor = 0
    bcolor = 0
    wwidth = 0
    llength = 0
    
    def __init__(self, x, y, r, g, b, w, l):
        self.x = x
        self.y = y
        self.rcolor = r
        self.gcolor = g
        self.bcolor = b
        self.wwidth = w
        self.llength = l
        
    def show(self):
        fill(self.rcolor, self.gcolor, self.bcolor)
        rect(self.x, self.y, self.llength, self.wwidth)
        
    def changeColor(self):
        t = random(1000)
        cr = noise(t+2)
        cg = noise(t+100)
        cb = noise(t+222)
        self.rcolor = map(cr,0,1,0,255)
        self.gcolor = map(cg,0,1,0,255)
        self.bcolor = map(cb,0,1,0,255)
    
    def move(self, x_speed, y_speed):
        self.x += x_speed
        self.y += y_speed

t=0
sticks = []
numberOfSticks = 500

def setup():
    global numberOfSticks, sticks
    size(800, 800)
    background(100)
    for i in range(numberOfSticks):
        w = random(50)
        l = random(150)
        x = random(width-l)
        y = random(height-w)
        r = random(255)
        g = random(255)
        b = random(255)
        stick = Stick(x,y,r,g,b,w,l)
        sticks.append(stick)
        
def draw():
    global sticks, t
    
    for stick in sticks:
        stick.show()
        stick.changeColor()
        x_speed = map(noise(t),0,1,-1,1)
        y_speed = map(noise(t+1000),0,1,-1, 1)
        stick.move(x_speed,y_speed)
        t += 0.001
