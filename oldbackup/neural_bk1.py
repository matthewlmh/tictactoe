# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 15:56:15 2022

@author: Man Hin Matthew Lui
"""

import pickle 
import pandas
import random

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" 
- 
-  class of the neural Network
- 
-  
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class neuralNetwork:

    ####################################################################################
    #
    # Var __init__
    # neuralCount        = the number of the neural
    # brain              = the list of the full neural node
    # stepList[]         = use in processThink, as the path of the node, pair with steplinkList
    # steplinkList[]     = use in processThink, as the path of the link, pair with stepList
    # awardRate          = use on the increase the award weight
    # lostRate           = use on the decrease the award weight
    # rejectRate         = use on the reject case, decrease the weight
    #
    ####################################################################################
    
    def __init__(self):
        self.neuralCount = 0 # 0 node, starter node
        self.brain=[]
        self.addNeural()
        self.stepList=[]
        self.steplinkList=[]
        self.awardBase = 500
        self.awardTop = 1000
        self.awardRound = 1
        self.awardRate = 0.01
        self.lostRate = 0.95
        self.rejectRate = 0.01
    
    
    
    ####################################################################################
    #
    # to add new neural to the brain
    # neuralID=X, will be same as the brain[X]
    #
    ####################################################################################
    def addNeural(self):   
        n = neural(self.neuralCount)
        self.brain.append(n)
        self.neuralCount+=1



    ####################################################################################
    #
    # start the think process
    # ini the stepList and steplinkList, they record the episode
    #
    ####################################################################################
    def startThink(self):
        self.stepList=[]
        self.stepList.append(0)  # 0 node, starter node
        self.steplinkList=[] 
    
        
    
    
    
    ####################################################################################
    #
    # process the thinking, has input and output
    # update stepList and steplinkList 
    #
    ####################################################################################
    def processThink(self,inputI):
        
        #debug use
        #print(len(self.stepList))
        
        
        temp = self.brain[self.stepList[ len(self.stepList)-1  ] ].procces(inputI) # call the lastest node in stepList to process
        
 
        if temp[3] is None:
            self.addNeural()
            self.stepList.append( self.neuralCount-1 )
            temp[3] = self.neuralCount-1
        else:
            self.stepList.append( temp[3] )
         
        self.steplinkList.append( temp )
        
        return temp[1]
    
    
    ####################################################################################
    #
    # use then reject, for Temporal Difference case
    #
    ####################################################################################
    def rejectThink(self): 
        
        index = len(self.steplinkList)-1
        # debug
        #print("index=" , index , "stepList=", len(self.stepList) )
        

        tempLink = self.steplinkList [ index ]
        tempNeuralID = self.stepList [ index ]
        
        # debug
        #print("tempLink=" , tempLink)
        #print("tempNeuralID=" , tempNeuralID)
        
        self.brain[tempNeuralID].linkList[ tempLink[0]  ][ tempLink[1] ][2] =  round( self.brain[tempNeuralID].linkList[ tempLink[0]  ][ tempLink[1] ][2] * self.rejectRate ,self.awardRound )
        self.brain[tempNeuralID].linkList[ tempLink[0]  ][ tempLink[1] ][3] = tempLink[3]
        
        # debug
        #print("before remove steplinkList=" , self.steplinkList)
        del self.steplinkList[-1]
        del self.stepList[-1]
        # debug
        #print("after remove steplinkList=" , self.steplinkList)
        
    
    ####################################################################################
    #
    # end the process, for Monte Carlo case, update every episode
    #
    ####################################################################################
    def endThink(self,winIND):     # winIND = Y/N

            
        for x1 in range(  len(self.steplinkList) ):
            inputI = self.steplinkList[x1][0]
            outputI = self.steplinkList[x1][1]
            outputNID = self.steplinkList[x1][3]
            neuralID = self.stepList[x1] 
            
            if winIND=="Y":
                d1 = self.brain[neuralID].linkList[inputI][outputI][2]
                self.brain[neuralID].linkList[inputI][outputI][2] = round(  d1 + ((self.awardTop - d1) * self.awardRate )  ,self.awardRound )
            else:
                d1 = self.brain[neuralID].linkList[inputI][outputI][2]
                self.brain[neuralID].linkList[inputI][outputI][2] = round(  d1 *  self.lostRate , self.awardRound )
                
                
                
            
            
            self.brain[neuralID].linkList[inputI][outputI][3] = outputNID

 
                
                # debug use
                # print( self.steplinkList[x1] )
                # print( inputI,outputI)
                # print( neuralID)
                # print( self.brain[neuralID].linkList[inputI] )

    
   
    ####################################################################################
    #
    # show the network map
    #
    ####################################################################################
    def showNeuralNetwork(self):
        totalN = len(self.brain)
        print("Total Neural = ",totalN)
        
        for x1 in range(totalN):
            for x2 in range( len(self.brain[x1].linkList ) ):
                print( self.brain[x1].neuralID, self.brain[x1].linkList[x2] )
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" 
- 
-  class of the neural
- 
-  
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class neural:

    ####################################################################################
    #
    # Var __init__
    # neuralID        = neural ID
    # linkList        = the link list for the nextNeural, [<input>] [<output>] [<input>,<output>,<weight>, <neural ID>], input=0 is the start.
    #                   eg. linkList[1][2] = [1,2,1.1,4531] 
    # outCombination  = the combination of the output
    # inCombination   = the combination of the input
    #
    ####################################################################################
   
    def __init__(self, ID):
        self.neuralID = ID
        self.outCombination = 10
        self.inCombination = 10 # should be 9, but 10 make it easy to do
        self.linkList = []
        for x1 in range(self.inCombination):
            self.linkList.append([])
            for y1 in range(self.outCombination):
                self.linkList[x1].append([x1,y1,1.0,None])

    ####################################################################################
    #
    # process the output by weight
    #
    ####################################################################################
    def procces(self,inputI):
        weight = []
        temp = []
        for x1 in range(self.outCombination-1):
            weight.append(  self.linkList[inputI][x1+1][2] )
            temp.append(   self.linkList[inputI][x1+1]  )

        return random.choices(temp, weights=weight, k=1)[0] 




"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
- 
-  test main
- 
- 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" 

## size test
# t1=[]
# for x1 in range(1000000):
#     t1.append( [x1,12,32,32323,x1] )
    
# filehandler = open("t1", 'wb') 
# pickle.dump(t1, filehandler)
# filehandler.close()



# column_names = ["ID", "I", "O","W","NID"]
# t2 = pandas.DataFrame(columns = column_names)
# j1 = []
# for x1 in range(1000000): 
#     j1.append(  {  'ID':x1 , 'I':12 , 'O':32 , 'W':32323 , 'NID': x1  })
# t2 = t2.append(j1, ignore_index=True) 

# filehandler = open("t2", 'wb') 
# pickle.dump(t2, filehandler)
# filehandler.close()

 

# t2.to_json("t3",orient="records")
 


# t2.to_csv("t4",index=False)




# neuralNetwork1 = neuralNetwork()
# neuralNetwork1.startThink()
# neuralNetwork1.processThink(0)
# neuralNetwork1.processThink(3) 
# neuralNetwork1.rejectThink()
# neuralNetwork1.endThink('Y')

# print( neuralNetwork1.neuralCount  )
# print( neuralNetwork1.brain[0].linkList[0]   )
# print( neuralNetwork1.brain[1].linkList[3]   )
# print( neuralNetwork1.brain[2].linkList[3]   )  






    
    