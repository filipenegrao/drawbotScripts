# Copyright (c) 2015 Filipe Negrão
# Version 0.1



#------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------

def draw_ruling(x,y):
    spaceBetween = 1.5*cm #space between ruling lines
    line((x, y), (x, y+xHeight+descender+ascender)) #vertical line
    line((x, y), (lineW, y)) # descender 
    line((x, y+descender), (lineW, y+descender)) # baseline
    line((x, y+xHeight+descender), (lineW, y+xHeight+descender)) #x-height
    line((x, y+xHeight+descender+ascender), (lineW, y+xHeight+descender+ascender))     

def draw_angle(angle,catop,start_x,start_y):
    stroke(.5)
    angleDegrees = 90-float(nib_angle)
    angleRad = radians(angleDegrees)
    catadj = tan(angleRad) * catop
    line((start_x,start_y), (catadj+start_x, catop+start_y))
    
    #text properties
    fill(0.7)
    font("Georgia")
    fontSize(10)
    txt = str(nib_angle)+"°"
    text(txt, (x+2.5*broadNib, y+descender+xHeight/2))

def draw_squares(x,y,broadNib):
    n = (xHeight+ascender+descender)/broadNib
    increment=0

    while n > 0:
        fill(0)
        if n == (xHeight+ascender+descender)/broadNib:
           rect(x,y,broadNib,broadNib)        
        elif (n%2)==0:
           rect(x,y+broadNib*increment,broadNib,broadNib)
        else:
            rect(x+broadNib,y+broadNib*increment,broadNib,broadNib)
        increment+=1
        n-=1


#------------------------------------------------------------
# SIZES
#------------------------------------------------------------

#convert cm and mm to pt 
cm = 28.3465
mm = 2.83465

#paper sizes
A4w, A4h = 297*mm, 210*mm
A3w, A3h = 297*mm, 420*mm

# create a new page and define it's format
size(A4w, A4h)

#------------------------------------------------------------
# UI
#------------------------------------------------------------

Variable([
    dict(name="nib_size", ui="EditText", args=dict(text="3.5")),
    dict(name="nib_angle", ui="EditText", args=dict(text="30")),
    dict(name="nib_angle_w", ui="Slider", 
            args=dict( 
                value=50, 
                minValue=10, 
                maxValue=200)),
    dict(name="xHeight", ui="EditText", args=dict(text="3.5")),
    dict(name="ascender", ui="EditText", args=dict(text="2.5")),
    dict(name="descender", ui="EditText", args=dict(text="2")),
    dict(name="X", ui="Slider", 
            args=dict( 
                value=2*cm, 
                minValue=1*cm, 
                maxValue=5*cm)),
    dict(name="Y", ui="Slider", 
            args=dict( 
                value=2*cm, 
                minValue=1*cm, 
                maxValue=5*cm))        
    ], globals())

#------------------------------------------------------------
# VARIABLES
#------------------------------------------------------------

#define your pen size
broadNib = float(nib_size) * mm

#define your ascender height
ascender = float(ascender) * broadNib

#define your x-height
xHeight = float(xHeight) * broadNib

#define your descender line
descender = float(descender) * broadNib

#define nib angle
nibAngle = float(nib_angle)

#define the weight of the lines considering a margin of 2cm
lineW = A4w-2*cm

#stroke color and width
stroke(0)
strokeWidth(.5)

#ruling total size
ruling = descender + xHeight + ascender

#margins
x=X
y=Y

#total nibs
n = (xHeight+ascender+descender)/broadNib

#broad nib angle's line 
angleDegrees = 90-float(nib_angle)
angle = radians(angleDegrees)

#------------------------------------------------------------
# LOOPS
#------------------------------------------------------------

while A4h>=0:
    spaceBetween = 1.5*cm #space between ruling lines
    draw_ruling(x,y)
    draw_angle(30,nib_angle_w,x,y+descender+xHeight/2)
    draw_squares(x,y,broadNib)
    
    y+=spaceBetween+xHeight+descender+ascender
    A4h = A4h-ruling-spaceBetween-2*cm

# save it as pdf on the current users desktop
#saveImage(["~/Desktop/001.pdf"])

