import maya.cmds as cmds
import random
from functools import partial

random.seed(1234)
    

#main function that perfoms the actual processes
def instanceIteration(RotationRangeField, ScaleRangeEndField, ScaleRangeStartField, PlacementAmountField):
    
    #Takes user input from the gui and stores them into variables
    XRotationRange = cmds.floatFieldGrp(RotationRangeField, query = True, value1 - True)
    YRotationRange = cmds.floatFieldGrp(RotationRangeField, query = True, value2 - True)
    ZRotationRange = cmds.floatFieldGrp(RotationRangeField, query = True, value3 - True)
    RotationRange = [XRotationRange, YRotationRange, ZRotationRange]
    
    XScaleRangeEnd = cmds.floatFieldGrp(ScaleRangeEndField, query = True, value1 - True)
    YScaleRangeEnd = cmds.floatFieldGrp(ScaleRangeEndField, query = True, value2 - True)
    ZScaleRangeEnd = cmds.floatFieldGrp(ScaleRangeEndField, query = True, value3 - True)
    ScaleRangeEnd = [XScaleRangeEnd, YScaleRangeEnd, ZScaleRangeEnd]
    
    XScaleRangeStart = cmds.floatFieldGrp(ScaleRangeStartField, query = True, value1 - True)
    YScaleRangeStart  = cmds.floatFieldGrp(ScaleRangeStartField, query = True, value2 - True)
    ZScaleRangeStart  = cmds.floatFieldGrp(ScaleRangeStartField, query = True, value3 - True)
    ScaleRangeStart  = [XScaleRangeStart , YScaleRangeStart , ZScaleRangeStart]
    
    PlacementAmountFactor = cmds.floatField(PlacementAmountField, query = True, value - True)
    
    #get all the components to instance over
    #gets faces, edges and vertices
    components = cmds.filterExpand(selectionMask = (31,34,32))
            
    #get object that will be instanced
    objectlist = cmds.ls(selection = True, dagObjects = True , exactType = "mesh")
    object = objectlist[0]
    
    #Optional parameter that randomizes component placement
    if PlacementAmount != 1:
        PlacementAmount = (len(compenents)) * (PlacementAmountFactor) 
        components = random.choices(components, k = PlacementAmount)
    
        
 
    
    #iterate over each vertex, creating rivet and instance
    instanceGroupName=cmds.group(empty=True, name=object + "_instance_grp#")
    
    for component in components:
        cmds.select(deselect = True)
        currentInstance = cmds.instance(object, name = object + "_instance#")
        cmds.parent(currentInstance, instanceGroupName)
        cmds.select(component, currentInstance , add = True)
        cmds.pointOnPolyConstraint(component, currentInstance)
        # calls function to randoimize instance if requested
        instanceRandomizer(currentInstance, RotationRange, ScaleRangeEnd, ScaleRangeStart, PlacementAmountFactor)
# Optional settings to randomize instances
def instanceRandomizer(currentInstance, RotationRange, ScaleRangeEnd, ScaleRangeStart, PlacementAmountFactor):
    
    xRot=random.uniform(0, RotationRange[0]) # this will be added to UI parameters
    yRot=random.uniform(0, RotationRange[1]) # this will be added to UI parameters
    zRot=random.uniform(0, RotationRange[2]) # this will be added to UI parameters
    cmds.rotate(xRot,yRot,zRot, currentInstance)
    xScale = random.uniform(ScaleRangeStart[0], ScaleRangeEnd[0]) # this will be added to UI parameters
    yScale = random.uniform(ScaleRangeStart[1], ScaleRangeEnd[1]) # this will be added to UI parameters
    zScale = random.uniform(ScaleRangeStart[2], ScaleRangeEnd[2]) # this will be added to UI parameters
    cmds.scale(xScale, yScale, zScale, currentInstance)
    cmds.xform(currentInstance,centerPivots=True)
    return currentInstance

#Create UI for script
def UI():
    global windowID
    windowID = 'myWindowID'
    
    if cmds.window( windowID, exists=True ):
        cmds.deleteUI( windowID )
    cmds.window( windowID, title = "PointonPolyConstraintInstancer", sizeable=False, resizeToFitChildren=True)
    cmds.rowColumnLayout(numberOfColumns = 4)
    
    cmds.separator( width=1, style='none' )
    cmds.text(label = "Random Rotation Range:", align = "right")
    cmds.separator( w=1, style='none' )
    RotationRangeField = cmds.floatFieldGrp( numberOfFields=3, value1 = 0, value2 = 0, value3 = 0 )
   
    cmds.separator( w=1, style='none' )
    cmds.text(label = "Random Scale Range:", align = "right")
    cmds.separator( width=1, style='none' )
    ScaleRangeField = cmds.floatFieldGrp( numberOfFields=3, value1 = 0, value2 = 0, value3 = 0 )
    
    cmds.separator( w=1, style='none' )
    cmds.text(label = "Random Component Placement Value:", align = "right")
    cmds.separator( width=1, style='none' )
    PlacementAmountField = cmds.floatField(value = 1, minValue = 0, maxValue = 1) 

    cmds.separator( w=1, style='none' )
    cmds.button(label="Apply", command=functools.partial(instanceIteration, RotationRangeField, 
                                                         ScaleRangeField, PlacementAmountField )) 
    cmds.button(label="Cancel")
    cmds.showWindow()

UI(instanceIteration)
