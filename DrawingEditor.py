from turtle import *
from kandinsky import draw_string as drawTxt, fill_rect as drawRect
from ion import *

BLACK,WHITE,GRAY,RED,GREEN,BLUE,YELLOW,PURPLE,ORANGE=(0,0,0),(255,255,255),(127,127,127),(240,10,10),(10,240,10),(10,10,240),(240,240,10),(240,10,240),(240,150,0)
coul=BLACK
psize=1
def k(k): return keydown(k)
def init():
  reset()
  showturtle()
  pendown()
  speed(10)
  colormode(255)
  penup()
def splash(c):
  color(c)
  pendown()
  pensize(psize)
  goto(position())
  penup()
  color(BLACK)
def ifsplash(c):
  if k(KEY_OK): splash(c)
def moove():
  if k(KEY_UP):
    goto(position()[0],position()[1]+1)
  if k(KEY_DOWN):
    goto(position()[0],position()[1]-1)
  if k(KEY_RIGHT):
    goto(position()[0]+1,position()[1])
  if k(KEY_LEFT):
    goto(position()[0]-1,position()[1])
def pSizeSwitch():
  global psize
  if k(KEY_ZERO):
    if psize==1:
      pensize(25)
      psize=25
    else:
      pensize(1)
      psize=1
    while k(KEY_ZERO): continue
def coulSwitch():
  global coul
  if k(KEY_ONE):coul=BLACK
  if k(KEY_TWO):coul=WHITE
  if k(KEY_THREE):coul=GRAY
  if k(KEY_FOUR):coul=RED
  if k(KEY_FIVE):coul=GREEN
  if k(KEY_SIX):coul=BLUE
  if k(KEY_SEVEN):coul=YELLOW
  if k(KEY_EIGHT):coul=PURPLE
  if k(KEY_NINE):coul=ORANGE
def drawCol():
  drawTxt("color:",5,5)
  drawRect(80,5,20,20,coul)
def drawSize():
  drawTxt("       ",120,5)
  drawTxt("size:"+str(psize),120,5)
def ifInit():
  if keydown(KEY_EXE):
    init()

init()
while 1:
  ifInit()
  moove()
  pSizeSwitch()
  coulSwitch()
  ifsplash(coul)
  drawCol()
  drawSize()
