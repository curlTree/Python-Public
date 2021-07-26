# def check():
#          a=int(input('Enter a number'))
#          if a%2==0: print("Even")
#          else: print("Odd")
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import time
x=np.linspace(0,20,21)
y=np.linspace(0,20,21)
plt.xticks(range(0,20,2))
plt.yticks(range(0,20,2))
class bot():
    extent=[1,2,1,2]
    lb=0
    rb=0
    face=0
    token_picked=[]
    token_board=[]
    token_count=0
    def __init__(self,token_loc):
        self.cbot_img=Image.open('Ghotul.png')
        self.token=Image.open('token.png')
        
        fig=plt.figure(figsize=(8,8))
        for i in x:
            for j in y:
                plt.plot(i,j,'r+');
        plt.savefig('grid.png')
        plt.gca().axis([0,20,0,20]);
        self.grid=Image.open('grid.png')
        self.token_board=token_loc
        self.show_tokens()
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
        self.extent[self.lb]+=self.sgn*1
        self.extent[self.rb]+=self.sgn*1
        self.gridify()
    def turn_left(self):
#         self.cbot_img=
        v=self.cbot_img.rotate(90)
#         print(self.cbot_img)
        self.cbot_img=v
        self.face+=1
        self.face=self.face % 4
        self.gridify()
#         return self.cbot_img
    def pick_token(self):
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
    def drop_token(self):    
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
#         print(self.extent,self.token_board)
        plt.imshow(self.cbot_img,extent=self.extent,alpha=0.8)
        plt.show()
#         time.sleep(1)
#         for i in x:
#             for j in y:
#                 plt.plot(i,j,'r+');
