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
        self.stepList=[]
        self.steplinkList=[]
        self.awardBase = 500.00
        self.awardTop = 1000.00
        self.awardRound = 1
        self.awardRate = 0.01
        self.lostRate = 0.95
        self.rejectRate = 0.01
        self.addNeural()
        

        
        
        
    
    
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
        
        
        #
        #print(temp)
        #print( self.brain[0].linkList  )
        
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
        
        i = tempLink[0]
        o = tempLink[1]
        w = tempLink[2]
        nid = tempLink[3]
        
 
            
        # debug
        #print("tempNeuralID=",tempNeuralID)
        #print("o=",o)
        #print(self.brain[tempNeuralID].linkList[  (self.brain[tempNeuralID].linkList["I"] == i) & (self.brain[tempNeuralID].linkList["O"] == o)  ]) 
        # if  len(self.brain[tempNeuralID].linkList[ (self.brain[tempNeuralID].linkList["I"] == i) & (self.brain[tempNeuralID].linkList["O"] == o) ] ) == 0:
        #     print("---- error -----")
        #     print(tempNeuralID)
        #     print(tempLink)
        
        self.brain[tempNeuralID].linkList.loc[ (self.brain[tempNeuralID].linkList["I"] == i) & (self.brain[tempNeuralID].linkList["O"] == o) ,["W"] ] =  round( w * self.rejectRate ,self.awardRound )
        self.brain[tempNeuralID].linkList.loc[ (self.brain[tempNeuralID].linkList["I"] == i) & (self.brain[tempNeuralID].linkList["O"] == o) ,["NID"] ] =  nid      
 
        
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

        #debug
        #print("len(self.steplinkList)=",len(self.steplinkList))
   
        for x1 in range(  len(self.steplinkList) ):
            inputI = self.steplinkList[x1][0]
            outputI = self.steplinkList[x1][1]
            weightI = self.steplinkList[x1][2]
            outputNID = self.steplinkList[x1][3]
            neuralID = self.stepList[x1] 
            
            # debug
            # print( "endThink update:" ,  neuralID ,  inputI, outputI , weightI , outputNID)
       
            
            if winIND=="Y":
                self.brain[neuralID].linkList.loc[ (self.brain[neuralID].linkList["I"] == inputI) & (self.brain[neuralID].linkList["O"] == outputI) ,["W"] ] = round(  weightI + ((self.awardTop - weightI) * self.awardRate )  ,self.awardRound )
            elif winIND=="N":
                self.brain[neuralID].linkList.loc[ (self.brain[neuralID].linkList["I"] == inputI) & (self.brain[neuralID].linkList["O"] == outputI) ,["W"] ] = round(  weightI *  self.lostRate , self.awardRound )
                
                
                
            self.brain[neuralID].linkList.loc[ (self.brain[neuralID].linkList["I"] == inputI) & (self.brain[neuralID].linkList["O"] == outputI) ,["NID"] ] =  outputNID      
     
            
 
            

                
            # debug use
            # print( self.steplinkList[x1] )
            # print( inputI,outputI)
            #print( weightI)
            #print( round(  weightI + ((self.awardTop - weightI) * self.awardRate )  ,self.awardRound ) )

 

     
   
    ####################################################################################
    #
    # show the network map
    #
    ####################################################################################
    def showNeuralNetwork(self):
        totalN = len(self.brain)
        print("Total Neural = ",totalN)
        
        if totalN>5:
            totalN=5
        
        for x1 in range(totalN):
            print( "------------- Neural ID = ",self.brain[x1].neuralID,"-------------" ) 
            print( self.brain[x1].linkList )
            
            
            
            
            

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
        self.outCombination = 9
        self.inCombination = 10 # should be 9, but 10 make it easy to do
        self.awardBase = 500.00
        column_names = [ "I", "O","W","NID"]
        self.linkList = pandas.DataFrame(columns = column_names)



    ####################################################################################
    #
    # process the output by weight
    #
    ####################################################################################
    def procces(self,inputI):
        
        
        # search the input
        tempD = self.linkList[self.linkList["I"] == inputI ]
        
        # add the tempD for random
        j1 = []
        for x1 in range(self.outCombination):
            
            # debug
            # print(len(tempD[tempD["O"] == x1+1 ]))
            
            if len(tempD[tempD["O"] == x1+1 ]) == 0:
                j1.append(  {   'I': inputI , 'O': x1+1 , 'W':self.awardBase , 'NID': None  } )

        if len(j1) != 0:
             tempD = tempD.append(j1, ignore_index=True) 

        #
        weight = tempD["W"].tolist()
        temp = tempD["O"].tolist()
        
        
        
 

        #
        i = inputI
        if sum(weight)==0:
            for x1 in range (  len(weight)):
                weight[x1] = 1
        o = random.choices(temp, weights=weight, k=1)[0] 
        w = tempD[tempD["O"] == o ]["W"].tolist()[0]
        nid = tempD[tempD["O"] == o ]["NID"].tolist()[0]
        
 

        j1 = []
        j1.append(  {   'I': i , 'O': o , 'W':w , 'NID': nid  } )
        
        #
        #print(j1)
        if len(self.linkList[   (self.linkList["I"] == inputI )  &  (self.linkList["O"] == o)  ] ) == 0:
            #print( "procces insert:" ,  self.neuralID ,  i, o , w , nid) 
            self.linkList = self.linkList.append( j1, ignore_index=True ) 

        #
        #print (self.linkList)
        
        return [ i, o , w , nid  ]




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
# for  x1 in range(1000):
#     neuralNetwork1.startThink()
#     neuralNetwork1.processThink(0) 
#     neuralNetwork1.processThink(3) 
#     neuralNetwork1.rejectThink()
#     neuralNetwork1.endThink('Y')

# neuralNetwork1.showNeuralNetwork()


 


    