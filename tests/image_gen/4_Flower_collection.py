app.background = 'aliceBlue'

# vase
Oval(200, 300, 50, 10, fill='limeGreen')
Rect(175, 300, 50, 100, fill='silver')
Oval(200, 370, 100, 135,
     fill=gradient('gray', 'silver', 'silver', start='left-bottom'))

def drawLeaf(mouseX, mouseY):
    Star(mouseX, mouseY, 30, 4, fill='green', rotateAngle=45)

def drawFlower(mouseX, mouseY):
    Line(mouseX, mouseY, 200, 300, fill='limeGreen', lineWidth=4)
    Star(mouseX, mouseY, 25, 6, fill=gradient('lavender', 'plum', 'plum'))
    Circle(mouseX, mouseY, 9, fill='lemonChiffon')

def onMousePress(mouseX, mouseY):
    if (mouseY > 200):
        drawLeaf(mouseX, mouseY)
    drawFlower(mouseX, mouseY)

onMousePress(60, 199)
onMousePress(100, 200)
onMousePress(200, 200)
onMousePress(250, 201)


# -
app.background = 'aliceBlue'

# vase
Oval(200, 300, 50, 10, fill='limeGreen')
Rect(175, 300, 50, 100, fill='silver')
Oval(200, 370, 100, 135,
     fill=gradient('gray', 'silver', 'silver', start='left-bottom'))

def drawLeaf(mouseX, mouseY):
    Star(mouseX, mouseY, 30, 4, fill='green', rotateAngle=45)

def drawFlower(mouseX, mouseY):
    Line(mouseX, mouseY, 200, 300, fill='limeGreen', lineWidth=4)
    Star(mouseX, mouseY, 25, 6, fill=gradient('lavender', 'plum', 'plum'))
    Circle(mouseX, mouseY, 9, fill='lemonChiffon')

def onMousePress(mouseX, mouseY):
    if (mouseY > 200):
        drawLeaf(mouseX, mouseY)
    drawFlower(mouseX, mouseY)

onMousePress(60, 199)
onMousePress(100, 200)
onMousePress(200, 200)
onMousePress(250, 201)


# -
app.background = 'aliceBlue'

# vase
Oval(200, 300, 50, 10, fill='limeGreen')
Rect(175, 300, 50, 100, fill='silver')
Oval(200, 370, 100, 135,
     fill=gradient('gray', 'silver', 'silver', start='left-bottom'))

def drawLeaf(mouseX, mouseY):
    Star(mouseX, mouseY, 30, 4, fill='green', rotateAngle=45)

def drawFlower(mouseX, mouseY):
    Line(mouseX, mouseY, 200, 300, fill='limeGreen', lineWidth=4)
    Star(mouseX, mouseY, 25, 6, fill=gradient('lavender', 'plum', 'plum'))
    Circle(mouseX, mouseY, 9, fill='lemonChiffon')

def onMousePress(mouseX, mouseY):
    if (mouseY > 200):
        drawLeaf(mouseX, mouseY)
    drawFlower(mouseX, mouseY)

