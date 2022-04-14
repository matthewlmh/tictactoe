# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:53:12 2022

@author: Man Hin Matthew Lui
"""
from neural import * 


#import random
import pickle 
import zipfile
import os
import time


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
- 
-  class of the ant
- 
- 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" 

class ant:

    def __init__(self
                 ,name
                 ,impName = None
                 ,awardBase=500.00
                 ,awardTop=1000.00
                 ,awardRound=1
                 ,awardRate=0.01
                 ,lostRate=0.95
                 ,rejectRate=0.01
                 ):
        self.name = name
        self.winTimes = 0
        self.impName=impName
        
        self.awardBase = awardBase
        self.awardTop = awardTop
        self.awardRound = awardRound
        self.awardRate = awardRate
        self.lostRate = lostRate
        self.rejectRate = rejectRate
            
        if impName is None:
            self.loadedNeuralNetwork = neuralNetwork(self.awardBase
                                                    ,self.awardTop
                                                    ,self.awardRound
                                                    ,self.awardRate
                                                    ,self.lostRate
                                                    ,self.rejectRate)
        else:
            self.importNeuralNetwork(impName
                                     ,awardBase
                                     ,awardTop
                                     ,awardRound
                                     ,awardRate
                                     ,lostRate
                                     ,rejectRate
                                     )
        

            
        self.getNextStepTime = 0.00
        self.rejectStepTime = 0.00
        self.startGameTime = 0.00
        self.endGameTime = 0.00
        
        
    def getNextStep(self,inputI):
        start = time.time()
        r = self.loadedNeuralNetwork.processThink(inputI)
        stop = time.time()
        self.getNextStepTime += (stop-start)
        return r

    def rejectStep(self):
        start = time.time()
        self.loadedNeuralNetwork.rejectThink()
        stop = time.time()
        self.rejectStepTime += (stop-start)
       


    def startGame(self):
        start = time.time()
        self.loadedNeuralNetwork.startThink()
        stop = time.time()
        self.startGameTime += (stop-start)
        
        

    def endGame(self,winIND):
        start = time.time()
        self.loadedNeuralNetwork.endThink(winIND)
        stop = time.time()
        self.endGameTime += (stop-start)
        
        
        
    def showLoadedNeuralNetwork(self):
        self.loadedNeuralNetwork.showNeuralNetwork()
        
        
    def exportNeuralNetwork(self,expName):
        filehandler = open(expName + ".tmp", 'wb') 
        pickle.dump(self.loadedNeuralNetwork, filehandler)
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
          
        
        
    def importNeuralNetwork(self,impName):
         
        zip_file = zipfile.ZipFile(impName, mode='r')
        zip_file.extract(impName + '.tmp' )
        zip_file.extractall( )
        zip_file.close()

  
        self.impName = impName
        filehandler = open(impName  + '.tmp'  , 'rb') 
        self.loadedNeuralNetwork = pickle.load( filehandler)
        filehandler.close()    

        if os.path.exists(impName + ".tmp"):
            os.remove(impName + ".tmp")
        else:
            print("The file does not exist")
            
        
    def exportNeuralNetworkCSV(self,expName):
        
        column_names1 = [ "I", "O","W","NID"]
        tempList = pandas.DataFrame(columns = column_names1)
        
        column_names2 = [ "ID","I", "O","W","NID"]
        mainList = pandas.DataFrame(columns = column_names2)
        
        total = len(self.loadedNeuralNetwork.brain)
        
        for x1 in range (  len(self.loadedNeuralNetwork.brain)    ):
           tempList = tempList.append( self.loadedNeuralNetwork.brain[x1].linkList, ignore_index=True)
           tempList.insert(0, "ID", x1)
           mainList = mainList.append( tempList , ignore_index=True)
           tempList = pandas.DataFrame(columns = column_names1)
           if x1>=10:
               for y in range(9):
                   if round( (y+1) * 0.1 * total )==x1 and x1%10 :
                       print( str((y+1)) + "0%....") 
 

        mainList.to_csv(expName ,index=False)
        
        
        

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
- 
-  test main
- 
- 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" 

 
 



# zf = zipfile.ZipFile("an1", mode='w', compression=zipfile.ZIP_DEFLATED)

# ## Add a file to the archive
# zf.write("an1.tmp")

# ## Close the archive releasing it from memory
# zf.close()

# if os.path.exists("an1.tmp"):
#     os.remove("an1.tmp")
# else:
#     print("The file does not exist")
  
  

# zip_file = zipfile.ZipFile('an1', mode='r')
# zip_file.extract('an1.tmp' )
# zip_file.extractall( )
# zip_file.close()

 
  









        