"""
conway.py
Author: Dimitri
Credit: Morgan
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
"""
from ggame import App, Color, Sprite, RectangleAsset, LineStyle, MouseEvent

purple = Color(0x512DA8, 1)
colortwo = Color(0xFF0000, 1)
nostroke = LineStyle(0, purple)
livecells = {}
makecells = []
surcells = []
killcells = {}
xdiff = 0
ydiff = 0

def create():
    for celle in makecells[:]:
        Cell((celle[0], celle[1]))
        makecells.remove(celle)

def getcoor(xx, yy):
    return([[xx - 10, yy - 10], [xx - 10, yy], [xx - 10, yy + 10], [xx, yy - 10], [xx, yy + 10], [xx + 10, yy - 10], [xx + 10, yy], [xx + 10, yy + 10]])

def check():
    for celle in surcells[:]:
        if find(celle[0], celle[1]) == 3:
            makecells.append(celle)
        surcells.remove(celle)
            
def checking(xx, yy):
    dei = getcoor(xx, yy)
    for deadcell in dei:
        if livecells.get((deadcell[0], deadcell[1]), False) == False:
            if deadcell in surcells:
                at = 1
            else:
                surcells.append(deadcell)
            
def find(xx, yy):
    neighbors = getcoor(xx, yy)
    neighborcount = 0
    for posi in neighbors:
        if livecells.get((posi[0], posi[1]), False) == True:
            neighborcount += 1
    return(neighborcount)

class Cell(Sprite):
    pix = RectangleAsset(10, 10, nostroke, purple)
    
    def __init__(self, position):
        super().__init__(Cell.pix, position)
        self.ogposx = self.x
        self.ogposy = self.y
        livecells[(self.ogposx, self.ogposy)] = True
        self.x += xdiff
        self.y += ydiff
        self.day = 0
        self.changed = False
        
    def step(self):
        if livecells.get((self.ogposx, self.ogposy)) == True:
            self.day += 1
            if self.day > 1 and self.changed == False:
                self.color = colortwo
                self.changed = True
            n = find(self.ogposx, self.ogposy)
            if n < 2 or n > 3:
                killcells[(self.ogposx, self.ogposy)] = True
            checking(self.ogposx, self.ogposy)
        else:
            self.visible = False
    
    def kill(self):
        if killcells.get((self.ogposx, self.ogposy), False) == True:
            livecells[(self.ogposx, self.ogposy)] = False
            killcells[(self.ogposx, self.ogposy)] = False
    
    def mover(self, direction):
        if direction == "r":
            self.x += 20
        elif direction == "l":
            self.x -= 20
        elif direction == "u":
            self.y -= 20
        elif direction == "d":
            self.y += 20
            
    def checktokill(self, px, py):
        if px == self.ogposx and py == self.ogposy:
            self.visible = False
            killcells[(self.ogposx, self.ogposy)] = True
            self.kill()

class Conway(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.stopped = True
        Cell((100, 50))
        Cell((110, 60))
        Cell((110, 70))
        Cell((100, 70))
        Cell((90, 70))
        self.listenKeyEvent("keydown", "right arrow", self.moveright)
        self.listenKeyEvent("keydown", "left arrow", self.moveleft)
        self.listenKeyEvent("keydown", "up arrow", self.moveup)
        self.listenKeyEvent("keydown", "down arrow", self.movedown)
        self.listenKeyEvent("keydown", "space", self.toggle)
        self.listenMouseEvent('click', self.create)
        
    def moveright(self, event):
        xdiff += 20
        for cell in self.getSpritesbyClass(Cell):
            cell.mover("r")
    def moveleft(self, event):
        xdiff -= 20
        for cell in self.getSpritesbyClass(Cell):
            cell.mover("l")
    def moveup(self, event):
        ydiff -= 20
        for cell in self.getSpritesbyClass(Cell):
            cell.mover("u")
    def movedown(self, event):
        ydiff += 20
        for cell in self.getSpritesbyClass(Cell):
            cell.mover("d")
    def toggle(self, event):
        if self.stopped == True:
            self.stopped = False
        else:
            self.stopped = True
            
    def create(self, event):
        diffx = event.x % 10
        diffy = event.y % 10
        finx = event.x - diffx - 10 - xdiff
        finy = event.y - diffy - 10 - ydiff
        if livecells.get((finx, finy), False) == True:
            for cell in self.getSpritesbyClass(Cell):
                cell.checktokill(finx, finy)
        else:
            Cell((finx, finy))
    
    def step(self):
        if self.stopped == False:
            create()
            for cell in self.getSpritesbyClass(Cell):
                cell.kill()
            for cell in self.getSpritesbyClass(Cell):
                cell.step()
            check()
        
        
myapp = Conway(640, 480)
myapp.run()
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

black = Color(0, 1)
white = Color(0xffffff, 1)
noline = LineStyle(0, white)
livecells = {}
deadcells = {}

def neighborlist(x1, y1):
    return([[x1-10, y1-10], [x1-10, y1], [x1-10, y1+10], [x1, y1-10], [x1, y1+10], [x1+10, y1-10], [x1+10, y1], [x1+10, y1+10]])

def getneighbors(x1, y1):
    neighbors = neighborlist(x1, y1)
    counted = 0
    for outsidecells in neighbors:
        if livecells.get((outsidecells[0], outsidecells[1]), False) == True:
            counted += 1
    return(counted)


class Cell(Sprite):
    asset = RectangleAsset(10, 10, noline, black)
    
    def __init__(self, position):
        super().__init__(Cell.asset, position)
        livecells[(self.x, self.y)] = True
        generation = 0
        
    def step(self):
        if livecells.get((self.x[0], self.y[1]), False) == True:
            self.generation += 1
            neighbors = getneighbors(self.x, self.y)
            if neighbors < 2 or neighbors > 3:
                self.visible == False
        print(0)



class Conways(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        #self.stopped = True
        Cell((100, 100))
        Cell((90, 100))
        Cell((110, 100))


    def step(self):
      #  for cell in self.getSpritesbyClass(Cell):
      #      cell.kill()
        for cell in self.getSpritesbyClass(Cell):
            cell.step()




myapp = Conways(640, 480)
myapp.run()
