import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import time
x=np.linspace(0,20,21)
y=np.linspace(0,20,21)

class bot():
    extent=[1,2,1,2]
    lb=0
    rb=0
    face=0
    token_picked=[]
    token_board=[]
    token_count=0
    _left_wall=0
    _right_wall=np.max(x)
    _top_wall=np.max(y)
    _bottom_wall=0
    def __init__(self,token_loc,max_x,max_y):
        self.x=np.linspace(0,max_x,max_x+1)
        self.y=np.linspace(0,max_y,max_y+1)
        # print(self.x,self.y)
        self.cbot_img=Image.open('Ghotul.png')
        self.token=Image.open('token.png')
        
        plt.figure(figsize=(8,8))
        for i in self.x:
            for j in self.y:
                plt.plot(i,j,'r+')
        plt.savefig('grid.png')
        plt.gca().axis([0,max_x,0,max_y])
        plt.xticks(range(0,max_x,2))
        plt.yticks(range(0,max_y,2))
        self.grid=Image.open('grid.png')
        self.token_board=token_loc
        self.show_tokens()
    def right_wall(self):
        if self.face==0 and self.extent[1]>=self._right_wall:
            return True
        else:
            return False
    def left_wall(self):
        if self.face==2 and self.extent[0]<=self._left_wall:
            return True
        else:
            return False    
    def top_wall(self):
        if self.face==1 and self.extent[3]>=self._top_wall:
            return True
        else:
            return False     
    def bottom_wall(self):
        if self.face==3 and self.extent[2]<=self._bottom_wall:
            return True
        else:
            return False
    def front_is_clear(self):
        for t in self.token_board:
            if (self.right_wall() or self.face==0 and (self.extent[0]+1==t[0] and self.extent[1]+1==t[1] and self.extent[2]==t[2] and self.extent[3]==t[3])):
                    # print('face0',self.extent,t[0])
                    return False
            elif (self.top_wall() or self.face==1 and (self.extent[0]==t[0] and self.extent[1]==t[1] and self.extent[2]+1==t[2] and self.extent[3]+1==t[3])):
                    # print('face1',self.extent,t[3])
                    return False
            elif (self.left_wall() or self.face==2 and (self.extent[0]-1==t[0] and self.extent[1]-1==t[1] and self.extent[2]==t[2] and self.extent[3]==t[3])):
                    # print('face2',self.extent,t[3])
                    return False
            elif (self.bottom_wall() or self.face==3 and (self.extent[0]==t[0] and self.extent[1]==t[1] and self.extent[2]-1==t[2] and self.extent[3]-1==t[3])):
                    # print('face3',self.extent,t[3])
                    return False    
        return True
    def move(self):
        if  self.face==0:
            self.lb=0
            self.rb=1
            self.sgn=1
        elif  self.face==1:
            self.lb=2
            self.rb=3
            self.sgn=1
        elif  self.face==2:
            self.lb=0
            self.rb=1
            self.sgn=-1
        elif  self.face==3:
            self.lb=2
            self.rb=3   
            self.sgn=-1
        p_lb=self.extent[self.lb]
        p_rb=self.extent[self.rb]
        self.extent[self.lb]+=self.sgn*1
        self.extent[self.rb]+=self.sgn*1    
        if ((self.face==0 and self.extent[1]>self._right_wall) or (self.face==2 and self.extent[0]<self._left_wall) or (self.face==3 and self.extent[2]<self._bottom_wall) or (self.face==1 and self.extent[3]>self._top_wall)):
            print("beyond boundary")
            self.extent[self.lb]=p_lb
            self.extent[self.rb]=p_rb
        self.show_tokens()
    def turn_left(self):
#         self.cbot_img=
        v=self.cbot_img.rotate(90)
#         print(self.cbot_img)
        self.cbot_img=v
        self.face+=1
        self.face=self.face % 4
        self.show_tokens()
#         return self.cbot_img
    def pick_egg(self):
        indx=-1
        found=-1
        for t in self.token_board:
            indx+=1
            if t[2]==self.extent[2] and t[3]==self.extent[3] and t[1]==self.extent[1] and t[0]==self.extent[0]:
                    found=indx
#                     print(self.extent,'found at:',indx)
        if found>-1:
            self.token_picked.append(self.token)
            self.token_board=[v for i,v in enumerate(self.token_board) if i!=found]
#             print(self.token_board,indx)
        self.show_tokens()
    def drop_egg(self):    
#         self.token_picked.pop()
        self.token_board.append(self.extent.copy())
        self.show_tokens()
    def show_tokens(self):
#         plt.figure(figsize=(8,8))
        plt.imshow(self.grid)
        for t in self.token_board:
            plt.imshow(self.token,extent=t)
        self.gridify()
    def gridify(self):
        # print(self.extent,self.token_board)
        plt.imshow(self.cbot_img,extent=self.extent,alpha=0.8)
        plt.show()
#         time.sleep(1)
#         for i in x:
#             for j in y:
#                 plt.plot(i,j,'r+');
    def __str__(self):
        print(self.extent)
