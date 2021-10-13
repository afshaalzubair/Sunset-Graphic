
from Graphics import *
from random import *

def drawOcean():
   setColor("indianred")
   fillArc(650,800,1300,550,270,90)
   
def drawDetail():
   DetailX = randint(0,1300)
   DetailY = randint(350,700)
   setColor("lightcoral")
   for k in range(100):
      drawString("~",DetailX,DetailY,"Freestyle Script",36,"normal")
      DetailX = randint(0,1300)
      DetailY = randint(350,700)