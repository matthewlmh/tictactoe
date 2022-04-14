# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:55:07 2022

@author: Man Hin Matthew Lui
"""

from ant import *
from tictactoe import * 

import random
import time



"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
- 
-  class of the training
- 
- 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" 


class training:
    
    
    
    ####################################################################################
    #
    # Var __init__
    # ant1          = artificial neural terminal (ANT) class, the player 1
    # ant2          = artificial neural terminal (ANT) class, the player 2
    #
    ####################################################################################
    def __init__(self): 
        
        ant1 = ant("an1"
                   ,None # impName
                   ,500.00 # awardBase
                   ,1000.00 # awardTop
                   ,1 # awardRound
                   ,0.5 # awardRate
                   ,0.5 # lostRate
                   ,0.01 # rejectRate
                   )
        ant2 = ant("an2"
                   ,None # impName
                   ,500.00 # awardBase
                   ,1000.00 # awardTop
                   ,1 # awardRound
                   ,0.5 # awardRate
                   ,0.5 # lostRate
                   ,0.01 # rejectRate
                   )
        self.ant = [ ant1 , ant2 ]
        self.menu()
        
    
    ####################################################################################
    #
    # play the game 1 time
    #
    ####################################################################################
    def play(self):
        
        
        
        self.tictactoe1 = tictactoe( self.ant[0].name 
                                    ,self.ant[1].name )
        
        ###############################
        # start the game, to start with the 1st neural
        ###############################        
        self.ant[0].startGame()
        self.ant[1].startGame()
        
        
        ###############################
        # process the game
        ###############################            
        previousStep = 0
        currentStep = 0
        while self.tictactoe1.winPlayer == -1: 
            
            
            ###############################
            # use previousStep to call getNextStep, get the next step
            # play the tictactoe1 step by step by player
            ###############################    
            currentStep = self.ant[ self.tictactoe1.currentPlayer-1  ].getNextStep(previousStep)
            getName = self.ant[ self.tictactoe1.currentPlayer-1  ].name  
            
            # debug use
            #print(self.tictactoe1.currentPlayer,getName,getNextStep)
            
            
            ###############################
            # input to tictactoe, check if the step ok
            ############################### 
            while  self.tictactoe1.inputStep2( getName ,currentStep) == -1:
                self.ant[ self.tictactoe1.currentPlayer-1  ].rejectStep()
                currentStep = self.ant[ self.tictactoe1.currentPlayer-1  ].getNextStep(previousStep)
                                             
            
            previousStep=currentStep
            self.tictactoe1.checkWin()
        
        
        
        #debug
        #self.tictactoe1.showttt()
        
        ###############################
        # call end game process for update the neural network
        ###############################
        if self.tictactoe1.winPlayer > 0:
            self.ant[ self.tictactoe1.winPlayer-1 ].winTimes += 1 
            
            if self.tictactoe1.winPlayer==1:
                self.ant[0].endGame('Y')
                self.ant[1].endGame('N')
 
            if self.tictactoe1.winPlayer==2:
                self.ant[0].endGame('N')
                self.ant[1].endGame('Y')   
        
        if self.tictactoe1.winPlayer == 0:
            self.ant[0].endGame('T')
            self.ant[1].endGame('T') 
        
        
    
    ####################################################################################
    #
    # menuImp
    #
    ####################################################################################
    def menuImp(self):
        
        i1 = ""
        while i1 != "0":
            print("-----------------------------------------------------------")
            print("Import for player 1 or 2?")
            print("1. Player 1")
            print("2. Player 2")
            print("0. Back")
            
            i1 = input()
            
            if i1 == "1":
                
                print("-----------------------------------------------------------")
                print("Please input the file name.")
                i2 = input()
                self.ant[0].importNeuralNetwork(i2) 
                
            elif i1 == "2":
                
                print("-----------------------------------------------------------")
                print("Please input the file name.")
                i2 = input()
                self.ant[1].importNeuralNetwork(i2) 
                
            elif i1 == "0":
                self.menu()
            else:
                pass
    

    ####################################################################################
    #
    # menuImp
    #
    ####################################################################################
    def menuExp(self):
        
        i1 = ""
        while i1 != "0":
            print("-----------------------------------------------------------")
            print("Export for player 1 or 2?")
            print("1. Player 1")
            print("2. Player 2")
            print("0. Back")
            
            i1 = input()
            
            if i1 == "1":
                
                print("-----------------------------------------------------------")
                print("Please input the file name.")
                i2 = input()
                self.ant[0].exportNeuralNetwork(i2) 
                
            elif i1 == "2":
                
                print("-----------------------------------------------------------")
                print("Please input the file name.")
                i2 = input()
                self.ant[1].exportNeuralNetwork(i2) 
                
            elif i1 == "0":
                self.menu()
            else:
                pass
    

    ####################################################################################
    #
    # menu1vs2
    #
    ####################################################################################
    def menu1vs2(self):
        start = time.time()
        
        for x1 in range(2):
            self.ant[x1].getNextStepTime = 0.00
            self.ant[x1].rejectStepTime = 0.00
            self.ant[x1].startGameTime = 0.00
            self.ant[x1].endGameTime = 0.00
        
        i1 = ""
 
        print("-----------------------------------------------------------")
        print("How many times?")
 
        
        i1 = input() 
        
        for x in range(int(i1)):
            self.play()
            if int(i1)>= 10:
                for y in range(9):
                    if round( (y+1) * 0.1 * int(i1))==x:
                        print( str((y+1)) + "0%....") 
        



        stop = time.time() 
        print("Total seconds of the run:", round(stop - start,2))
        for x1 in range(2):
            print("Player ", x1+1)
            print("getNextStepTime=" , round(self.ant[x1].getNextStepTime ,2) )
            print("rejectStepTime=" , round(self.ant[x1].rejectStepTime ,2) )
            print("startGameTime=" , round(self.ant[x1].startGameTime ,2) )
            print("endGameTime=" , round(self.ant[x1].endGameTime ,2) )

       

    ####################################################################################
    #
    # menuPWH
    #
    ####################################################################################
    def menuPWH(self):
        
        i1 = ""
        
        print("-----------------------------------------------------------")
        print("Play with player 1 or player 2?")
        print("1. Player 1")
        print("2. Player 2")
 
        i1=input()
        if i1=="1":
            playWithID = 0
        else:
            playWithID = 1
        
        
        self.tictactoe1 = tictactoe( self.ant[playWithID].name 
                                    ,"Human Player" )
        
        ###############################
        # start the game, to start with the 1st neural
        ###############################        
        self.ant[playWithID].startGame() 
        
        
        ###############################
        # process the game
        ###############################            
        previousStep = 0
        currentStep = 0
        while self.tictactoe1.winPlayer == -1: 
            
            
            ###############################
            # use previousStep to call getNextStep, get the next step
            # play the tictactoe1 step by step by player
            ###############################
            
            
            
            if self.tictactoe1.getCurrentPlayerName()==self.ant[playWithID].name:
                currentStep = self.ant[ playWithID  ].getNextStep(previousStep)
                getName = self.ant[ playWithID  ].name
            else:
                print("")
                
                # for debug use, show the related Neural
                # steplinkListNum = len(self.ant[ playWithID  ].loadedNeuralNetwork.steplinkList)
                # if steplinkListNum>0:
                #     nid = self.ant[ playWithID  ].loadedNeuralNetwork.steplinkList[steplinkListNum-1][3]   
                #     pandas.set_option('display.max_rows', 100)
                #     print( "------------- Neural ID = ",nid,"-------------" ) 
                #     print(self.ant[ playWithID  ].loadedNeuralNetwork.brain[nid].linkList.sort_values(by=['I', 'O']) )    
                # else:
                #     print( "------------- Neural ID = ",0,"-------------" ) 
                #     print(self.ant[ playWithID  ].loadedNeuralNetwork.brain[0].linkList.sort_values(by=['I', 'O']) )    
                
                self.tictactoe1.showttt()
                print("It is your move")
                i2 = input()
                currentStep = int(i2)
                getName = self.tictactoe1.getCurrentPlayerName()
            

            
            
            ###############################
            # input to tictactoe, check if the step ok
            ############################### 
            while  self.tictactoe1.inputStep2( getName ,currentStep) == -1:
                if self.tictactoe1.getCurrentPlayerName()==self.ant[playWithID].name:
                    self.ant[ self.tictactoe1.currentPlayer-1  ].rejectStep()
                    currentStep = self.ant[ self.tictactoe1.currentPlayer-1  ].getNextStep(previousStep)
                else:
                    print("")
                    self.tictactoe1.showttt()
                    print("It is your move")
                    i2 = input()
                    currentStep = int(i2)
                    getName = self.tictactoe1.getCurrentPlayerName()
                                             
            
            previousStep=currentStep
            self.tictactoe1.checkWin()
        
        
        
        
        
        ###############################
        # call end game process for update the neural network
        ###############################
        if self.tictactoe1.winPlayer > 0: 
            print("")
            self.tictactoe1.showttt()
            if self.tictactoe1.winPlayer==1:
                self.ant[playWithID].endGame('Y') 
                print("You lost!")
 
            if self.tictactoe1.winPlayer==2:
                self.ant[playWithID].endGame('N') 
                print("You win!")


    ####################################################################################
    #
    # exportAnt
    #player = 1 / 2
    #
    ####################################################################################        
    def exportAnt(self,player,expName): 
        filehandler = open(expName + ".tmp", 'wb') 
        pickle.dump(self.ant[player-1], filehandler)
        filehandler.close()
        
        zf = zipfile.ZipFile(expName, mode='w', compression=zipfile.ZIP_DEFLATED)

        ## Add a file to the archive
        zf.write(expName + ".tmp")
        
        ## Close the archive releasing it from memory
        zf.close()
        
        if os.path.exists(expName + ".tmp"):
            os.remove(expName + ".tmp")
        else:
            print("The file does not exist")
          

    def importAnt(self,player,impName): 
         
        zip_file = zipfile.ZipFile(impName, mode='r')
        zip_file.extract(impName + '.tmp' )
        zip_file.extractall( )
        zip_file.close()

  
        self.impName = impName
        filehandler = open(impName  + '.tmp'  , 'rb') 
        self.ant[player-1] = pickle.load( filehandler)
        filehandler.close()    

        if os.path.exists(impName + ".tmp"):
            os.remove(impName + ".tmp")
        else:
            print("The file does not exist")
            

    
    ####################################################################################
    #
    # menu
    #
    ####################################################################################
    def menu(self):
         
        i1 = ""
        
        while i1 != "0":
            print("-----------------------------------------------------------")
            print("Player 1:" , self.ant[0].name , "   Loaded File:" ,  self.ant[0].impName ," Win(this session):", self.ant[0].winTimes )
            print("   awardBase  :" , self.ant[0].awardBase )
            print("   awardTop   :" , self.ant[0].awardTop )
            print("   awardRound :" , self.ant[0].awardRound )
            print("   awardRate  :" , self.ant[0].awardRate )
            print("   lostRate   :" , self.ant[0].lostRate )
            print("   rejectRate :" , self.ant[0].rejectRate )
            print("Player 2:" , self.ant[1].name , "   Loaded File:" ,  self.ant[1].impName ," Win(this session):", self.ant[1].winTimes )
            print("   awardBase  :" , self.ant[1].awardBase )
            print("   awardTop   :" , self.ant[1].awardTop )
            print("   awardRound :" , self.ant[1].awardRound )
            print("   awardRate  :" , self.ant[1].awardRate )
            print("   lostRate   :" , self.ant[1].lostRate )
            print("   rejectRate :" , self.ant[1].rejectRate )
            print("-----------------------------------------------------------")
            print("")  
            print("What is the action?")  
            print("1. Import neural file for players")  
            print("2. Export neural file for players")
            print("3. Player 1 VS Player 2")
            print("4. Auto import Player 1/Player 2, use an1.nn/an2.nn   (only neuralNetwork)")
            print("5. Auto Export Player 1/Player 2, use an1.nn/an2.nn   (only neuralNetwork)")
            print("6. Auto Export Player 1/Player 2, use an1.csv/an2.csv (CSV)")
            print("7. Auto import Player 1/Player 2, use an1.ts/an2.ts   (with think setting)")
            print("8. Auto Export Player 1/Player 2, use an1.ts/an2.ts   (with think setting)")
            print("99. Play with human ")
            print("0. Exit")
            
            i1 = input()
            if i1 == "1":
                self.menuImp()
            elif i1 == "2":
                self.menuExp()
            elif i1 == "3":
                self.menu1vs2()
            elif i1 == "4":
                self.ant[0].importNeuralNetwork("an1.nn") 
                self.ant[1].importNeuralNetwork("an2.nn") 
            elif i1 == "5":
                self.ant[0].exportNeuralNetwork("an1.nn") 
                self.ant[1].exportNeuralNetwork("an2.nn") 
            elif i1 == "6":
                self.ant[0].exportNeuralNetworkCSV("an1.csv")  
                self.ant[1].exportNeuralNetworkCSV("an2.csv")  
            elif i1 == "7":
                self.importAnt(1, "an1.ts")
                self.importAnt(2, "an2.ts") 
            elif i1 == "8":
                self.exportAnt(1, "an1.ts")
                self.exportAnt(2, "an2.ts") 
            elif i1 == "99":
                self.menuPWH()
            elif i1 == "0":
                print("Bye!")
            elif i1 == "s":
                self.ant[0].showLoadedNeuralNetwork()
            else:
                pass
            
        

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
- 
-  unit test main
- 
- 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" 


 
training1 = training()

# i1=500.0
# for x in range(100):
#     i1 = i1 + ((1000- i1)*0.01)
#     print(i1)

# i1=500.0
# for x in range(100):
#     i1 = i1 * 0.95
#     print(i1)

# for x in range(1000):
#     training1.play()
#     #training1.tictactoe1.showttt() 

# ant1.exportNeuralNetwork("an1") 
# ant2.exportNeuralNetwork("an2") 

# print("ant1.winTimes=",ant1.winTimes)
# print("ant2.winTimes=",ant2.winTimes)

# print("---------------------------------------------------------------")
# ant1.showLoadedNeuralNetwork()
# print("---------------------------------------------------------------")
# ant2.showLoadedNeuralNetwork()

 