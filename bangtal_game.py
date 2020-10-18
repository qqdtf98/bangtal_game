from bangtal import *
from bangtal.singleton import *
from bangtal.game import *
import copy

scene1 = Scene("메인","images/main.png")
scene2 = Scene("게임","images/main.png")

selectedBlock = -1
top = 580
bottom = 100
start = 200
end = 680
selectedGame = ''
board = []

lv1 = Object("images/lv1.png")
lv1.locate(scene1, 200,450)
lv1.show()

lv2 = Object("images/lv2.png")
lv2.locate(scene1, 500,450)
lv2.show()

lv3 = Object("images/lv3.png")
lv3.locate(scene1, 800,450)
lv3.show()

background = Object("images/background.png")
background.locate(scene2,180,80)
background.show()



up = Object("images/up.png")
up.locate(scene2,950,190)
up.show()

down = Object("images/down.png")
down.locate(scene2,950,100)
down.show()

right = Object("images/right.png")
right.locate(scene2,1050,100)
right.show()

left = Object("images/left.png")
left.locate(scene2,850,100)
left.show()

select = Object("images/select.png")
select.locate(scene2, 870, 650)
select.show()

def lv1_onClick(x,y,action):
  global selectedGame
  selectedGame = 'lv1'
  setGame('lv1')
  scene2.enter()
lv1.onMouseAction = lv1_onClick

def lv2_onClick(x,y,action):
  global selectedGame
  selectedGame = 'lv2'
  setGame('lv2')
  scene2.enter()
lv2.onMouseAction = lv2_onClick


selected = Object("images/main.png")

class Block(Object):
  def onMouseClick(self,x,y,action):
    global selectedBlock
    selected.setImage(self._file)
    selected.locate(scene2,920,380)
    selected.show()
    selectedBlock = self.num
    
  def __init__(self,num,size,state,location,pos,file):
    id = GameServer.instance().createObject(file)
    ObjectManager.instance().register(id, self)

    print(file)
    self._file = file
    self.ID = id
    self.num = num
    self.size = size
    self.state = state
    self.location = location
    self.pos = pos
    self.onMouseAction = self.onMouseClick
    self.locate(scene2,location[0],location[1])



blockArr = []


def setGame(game):
  global board
  global blockArr
  if(game == 'lv1'):
    board = [[0,0,0,0,0,0,0],
             [0,0,0,0,1,1,1],
             [0,0,0,0,1,1,1],
             [0,0,1,1,1,1,1],
             [0,0,0,0,1,1,1],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]]
    blockArr = [Block(0,2,0,[360,340],[[3,2],[3,3]],"images/10.png"),
         Block(1,2,1,[520,340],[[2,4],[3,4]],"images/21.png"),
         Block(2,2,1,[600,340],[[2,5],[3,5]],"images/31.png"),
         Block(3,2,1,[680,340],[[2,6],[3,6]],"images/41.png"),
         Block(4,3,0,[520,500],[[1,4],[1,5],[1,6]],"images/50.png"),
         Block(5,3,0,[520,260],[[4,4],[4,5],[4,6]],"images/60.png")]
    for block in blockArr:
      block.show()
  elif (game == 'lv2'):
    board = [[0,0,0,0,0,0,0],
             [0,0,1,0,1,1,1],
             [0,0,1,0,1,0,1],
             [0,0,1,0,1,1,1],
             [0,0,1,0,1,0,1],
             [0,0,1,0,1,1,1],
             [0,0,0,0,0,0,0]]
    blockArr = [Block(0,2,0,[520,340],[[3,4],[3,5]],"images/10.png"),
             Block(1,2,1,[360,420],[[1,2],[2,2]],"images/21.png"),
             Block(2,2,1,[520,420],[[1,4],[2,4]],"images/31.png"),
             Block(3,2,0,[600,500],[[1,5],[1,6]],"images/40.png"),
             Block(4,3,1,[360,180],[[3,2],[4,2],[5,2]],"images/51.png"),
             Block(5,3,1,[680,260],[[2,6],[3,6],[4,6]],"images/61.png"),
             Block(6,2,1,[520,180],[[4,4],[5,4]],"images/71.png"),
             Block(7,2,0,[600,180],[[5,5],[5,6]],"images/80.png")]
    for block in blockArr:
      block.show()

def up_onClick(x,y,action):
  if(blockArr[selectedGame].state == 1):
    print(blockArr[selectedBlock]._file)
up.onMouseAction = up_onClick

def right_onClick(x,y,action):
  block = blockArr[selectedBlock]
  if(block.state == 0 and selectedBlock != -1 and block.pos[block.size-1][1]+1<7):
    if(block.location[0]+80<=end
       and board[block.pos[block.size-1][0]][block.pos[block.size-1][1]+1] == 0):
      block.locate(scene2,block.location[0]+80,block.location[1])
      board[block.pos[block.size-1][0]][block.pos[block.size-1][1]+1] = 1
      board[block.pos[block.size-1][0]][block.pos[block.size-1][1]-block.size+1] = 0
      block.location[0] += 80
      for i in range(0,block.size):
        block.pos[i][1] = block.pos[i][1]+1
right.onMouseAction = right_onClick

def left_onClick(x,y,action):
  block = blockArr[selectedBlock]
  if(block.state == 0 and selectedBlock != -1):
    if(block.location[0]-80>=start 
       and board[block.pos[0][0]][block.pos[0][1]-1] == 0):
      block.locate(scene2,block.location[0]-80,block.location[1])
      board[block.pos[0][0]][block.pos[0][1]-1] = 1
      board[block.pos[0][0]][block.pos[0][1]+block.size-1] = 0
      block.location[0] -= 80
      for i in range(0,block.size):
        block.pos[i][1] -= 1
left.onMouseAction = left_onClick

def up_onClick(x,y,action):
  block = blockArr[selectedBlock]
  if(block.state == 1 and selectedBlock != -1) and block.pos[0][0]!=0:
    if(block.location[1]+80<=top 
       and board[block.pos[0][0]-1][block.pos[0][1]] == 0):
      block.locate(scene2,block.location[0],block.location[1]+80)
      board[block.pos[0][0]-1][block.pos[0][1]] = 1
      board[block.pos[0][0]+block.size-1][block.pos[0][1]] = 0
      block.location[1] += 80
      for i in range(0,block.size):
        block.pos[i][0] -= 1
up.onMouseAction = up_onClick

def down_onClick(x,y,action):
  block = blockArr[selectedBlock]
  if(block.state == 1 and selectedBlock != -1):
    if(block.location[1]-80>=bottom 
       and board[block.pos[block.size-1][0]+1][block.pos[block.size-1][1]] == 0):
      block.locate(scene2,block.location[0],block.location[1]-80)
      board[block.pos[block.size-1][0]+1][block.pos[block.size-1][1]] = 1
      board[block.pos[block.size-1][0]-block.size+1][block.pos[block.size-1][1]] = 0
      block.location[1] -= 80
      for i in range(0,block.size):
        block.pos[i][0] += 1
down.onMouseAction = down_onClick

def printBoard():
  for i in range(0,7):
    for j in range(0,7):
      print(board[i][j],end='')
    print()
  print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')



startGame(scene1)