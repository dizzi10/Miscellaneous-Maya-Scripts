#Find Distance between two objects
import maya.cmds as cmds
from math import pow,sqrt
from itertools import combinations
objectList = cmds.ls(selection = True) 
def FindMatchingObjs(objectList):
    #This function taken from: http://www.timcallaway.com/?p=26
    def GetDistance(objA, objB):
    	gObjA = cmds.xform(objA, q=True, t=True, ws=True)
    	gObjB = cmds.xform(objB, q=True, t=True, ws=True)
    	
    	return( sqrt(pow(gObjA[0]-gObjB[0],2)+pow(gObjA[1]-gObjB[1],2)+pow(gObjA[2]-gObjB[2],2)) )
    
    def findobjAandObjB(matchedCombo,object):
        if object == matchedCombo[0]:
            objA = matchedCombo[0]
            objB = matchedCombo[1]
        else:
            objA = matchedCombo[1]
            objB = matchedCombo[0]
        return [objA , objB]
        
    #generate a list with every possible combination of objects
    uniqueCombinations=combinations(objectList,2)
    uniqueCombinationsList = list(uniqueCombinations)
    
    #Iterate through every possible combination and keep the ones with a common object for comparing distances
    distancedict = dict()
    matchedObjs = []
    
       
    for object in objectList:
        for value in matchedObjs:
            """if object in value: #why doesn't this work
                print object
                print"its working"
                continue"""
        combolst=[]
        
        for combo in uniqueCombinationsList: #create lists that all have a common object for comparison
            if object in combo:
                combolst.append(combo)
        
        for matchedCombo in combolst: #organize the lists so that object being compared is the first value
            ABlst = findobjAandObjB(matchedCombo,object)
            objA = ABlst[0]
            objB = ABlst[1]
            distancedict[matchedCombo] = GetDistance(objA, objB)
        
        matchedObjs.append(min(distancedict, key=distancedict.get))
        distancedict.clear()
    matchedObjsfinal = list(dict.fromkeys(matchedObjs)) #removes duplicates in list, because dicitonaries cannot have duplicate keys
    print(matchedObjsfinal)    

    
 
    