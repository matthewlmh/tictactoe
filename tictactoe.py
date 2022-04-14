# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 14:42:35 2022

@author: Man Hin Matthew Lui
"""


import random


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
- 
-  class of the tictactoe
- 
- 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" 

class tictactoe:

    
    ####################################################################################
    #
    # Var __init__
    # player        = store player name
    # ttt           = store the input for players, 0/1/2
    # currentPlayer = who turn? 1/2
    # winPlayer     = who win -1/0/1/2, -1 not end, 0 is tie(draw)
    # winCombo      = number to form a line to win
    #
    ####################################################################################
 
    
    def __init__(self, playerName1, playerName2):
        self.player = [ playerName1 ,playerName2]
        self.ttt = [ 
                     [0,0,0]
                    ,[0,0,0]
                    ,[0,0,0]
                   ]
        self.currentPlayer = random.randint(1, 2)
        self.winPlayer = -1
        self.winCombo = 3
        
        
   
    ####################################################################################
    #
    # show the tictactoe
    #
    ####################################################################################
    def showttt(self):
        tempX=1
        for x1 in range( len(self.ttt) ):
            for x2 in range( len(self.ttt) ):
                if self.ttt[x1][x2] == 0:
                    print( "\033[0;37;40m",tempX ,"\033[0;37;40m "  , end = '')
                if self.ttt[x1][x2] == 1:
                    print("\033[0;31;40m","X","\033[0;37;40m ", end = '')
                if self.ttt[x1][x2] == 2:
                    print("\033[0;36;40m","O","\033[0;37;40m ", end = '')
                tempX+=1
            print()
       
    
    ####################################################################################   
    #
    # function for check who is the winner
    # winPlayer     = who win -1/0/1/2, -1 not end, 0 is tie(draw)
    #
    ####################################################################################
    def checkWin(self): 
        tempCombo = 0
        ttt = self.ttt
        
        ###############################
        # check each player
        ###############################
        for tempCheckPlayer in range(1,3):
            
            
            
            ###############################
            # check row
            ###############################
            for x1 in range( len(ttt) ):
                tempCombo = 0
                for x2 in range( len(ttt) ):
                    if ttt[x1][x2]==tempCheckPlayer:
                        tempCombo+=1
         
                if tempCombo==self.winCombo:
                    self.winPlayer=tempCheckPlayer
                    break 
            if self.winPlayer != -1:
                break
            
            
            
            
            ###############################
            # check column       
            ###############################
            for x1 in range( len(ttt) ):
                tempCombo = 0
                for x2 in range( len(ttt) ):
                    if ttt[x2][x1]==tempCheckPlayer:
                        tempCombo+=1
         
                if tempCombo==self.winCombo:
                    self.winPlayer=tempCheckPlayer
                    break 
            if self.winPlayer != -1:
                break     
            
            ###############################
            # check X \
            ###############################
            tempX3=0
            for x1 in range( len(ttt) ):
                tempCombo = 0 
                for x2 in range( len(ttt) ): 
                    #print ( tempCheckPlayer ,  x2 , x2+tempX3  )
                    if x2+tempX3<len(ttt):
                        if ttt[x2][x2+tempX3]==tempCheckPlayer:
                            tempCombo+=1
                if tempCombo==self.winCombo:
                    self.winPlayer=tempCheckPlayer
                    break 
                tempX3+=1 
            if self.winPlayer != -1:
                break     
                            
            ###############################
            # check X /
            ###############################
            tempX3=0
            for x1 in range( len(ttt)):
                tempCombo = 0
                for x2 in range( len(ttt)  ): 
                    
                    # debug use
                    #print ( tempCheckPlayer, x2 ,  len(self.ttt) - 1 - x2 - tempX3  , "|", self.ttt[x2][len(self.ttt) - 1 - x2 - tempX3],tempCheckPlayer )
                    
                    if  len(ttt) - 1 - x2 - tempX3 >= 0:
                        if ttt[x2][len(ttt) - 1 - x2 - tempX3]==tempCheckPlayer: 
                            tempCombo+=1
                if tempCombo==self.winCombo:
                    self.winPlayer=tempCheckPlayer
                    
                    # debug use
                    #print("win=",self.winPlayer)
                    
                    break 
                tempX3+=1 
            if self.winPlayer != -1:
                break                 
            
            
        ###############################
        # check tie
        ###############################
        tempX3=0
        if self.winPlayer==-1:
            for x1 in range( len(ttt)):
                tempX3+=ttt[x1].count(0)
            if tempX3==0: 
                # debug use
                #print("--------tie?")
                self.winPlayer=0
                
                    

    ####################################################################################
    #
    # function for get the name of the current player
    # 
    ####################################################################################
    def getCurrentPlayerName(self):
        return self.player[  self.currentPlayer-1]
           


    ####################################################################################
    #
    # function for input the step
    # PI
    # playerName     = name of the player
    # pos1           = row 
    # pos2           = column
    #
    # PO
    # -1             = cannot put
    #  0             = ok
    #
    ####################################################################################
    def inputStep(self,playerName,pos1,pos2):
 
        
        if playerName != self.player[  self.currentPlayer-1]:
            return -1
        
        if pos1<0 or pos2<0 or  pos1>=len(self.ttt) or pos2>=len(self.ttt):
            return -1
        
        if self.ttt[pos1][pos2] != 0:
            return -1
        
        self.ttt[pos1][pos2] = self.currentPlayer
        
        self.currentPlayer+=1
        if self.currentPlayer>2:
            self.currentPlayer=1
        
        return 0






        

    ####################################################################################
    #
    # function for input the step
    #
    # PI
    # playerName     = name of the player
    # pos            = number 1-9   
    #
    # PO
    # -1             = cannot put
    #  0             = ok
    #
    ####################################################################################
    def inputStep2(self,playerName,pos):
        
         
        if pos<1 or pos>9:
            return -1
        
        if pos==1:
            pos1=0
            pos2=0

        if pos==2:
            pos1=0
            pos2=1
        
        if pos==3:
            pos1=0
            pos2=2
    
        if pos==4:
            pos1=1
            pos2=0
            
        if pos==5:
            pos1=1
            pos2=1
            
        if pos==6:
            pos1=1
            pos2=2

        if pos==7:
            pos1=2
            pos2=0
            
        if pos==8:
            pos1=2
            pos2=1
            
        if pos==9:
            pos1=2
            pos2=2            
            
            
        #print(playerName,pos1,pos2)   
        
        return self.inputStep(playerName,pos1,pos2)
        

          



"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""1
- 
-  unit test main
- 
- 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" 

# t = tictactoe("an1", "an2")   
# t.showttt()
# t.checkWin
 
# while t.winPlayer == -1:
#     print("Current Player=", t.currentPlayer , ", please enter...")
#     i1 = input()
#     print ( "input ok? (0=ok,-1=reject) ? ", t.inputStep2( t.getCurrentPlayerName(), int( i1) ) )
#     t.showttt()
#     t.checkWin()


# print ( 'winer =' , t.winPlayer)  





