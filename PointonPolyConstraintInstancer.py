import maya.cmds as cmds
import random
import functools

random.seed(1234)
    
#main function that perfoms the actual processes
def instanceIteration(RotationRangeField, ScaleRangeEndField, ScaleRangeStartField, PlacementAmountField, OffsetField, WeightField, *pArgs):
    
    #Takes user input from the gui and stores them into variables
    XRotationRange = cmds.floatFieldGrp(RotationRangeField, query = True, value1 = True)
    YRotationRange = cmds.floatFieldGrp(RotationRangeField, query = True, value2 = True)
    ZRotationRange = cmds.floatFieldGrp(RotationRangeField, query = True, value3 = True)
    RotationRange = [XRotationRange, YRotationRange, ZRotationRange]
    
    XScaleRangeEnd = cmds.floatFieldGrp(ScaleRangeEndField, query = True, value1 = True)
    YScaleRangeEnd = cmds.floatFieldGrp(ScaleRangeEndField, query = True, value2 = True)
    ZScaleRangeEnd = cmds.floatFieldGrp(ScaleRangeEndField, query = True, value3 = True)
    ScaleRangeEnd = [XScaleRangeEnd, YScaleRangeEnd, ZScaleRangeEnd]
    
    XScaleRangeStart = cmds.floatFieldGrp(ScaleRangeStartField, query = True, value1 = True)
    YScaleRangeStart  = cmds.floatFieldGrp(ScaleRangeStartField, query = True, value2 = True)
    ZScaleRangeStart  = cmds.floatFieldGrp(ScaleRangeStartField, query = True, value3 = True)
    ScaleRangeStart  = [XScaleRangeStart , YScaleRangeStart , ZScaleRangeStart]
    
    PlacementAmountFactor = cmds.floatField(PlacementAmountField, query = True, value = True)
    
    Xoffsetamount = cmds.floatFieldGrp(OffsetField, query = True, value1 = True)
    Yoffsetamount = cmds.floatFieldGrp(OffsetField, query = True, value2 = True)
    Zoffsetamount = cmds.floatFieldGrp(OffsetField, query = True, value3 = True)
    
    weightAmount = cmds.floatSliderGrp(WeightField, query = True, value = True)
    
    #get all the components to instance over
    #gets faces, edges and vertices
    components = cmds.filterExpand(selectionMask = (31,34,32))
            
    #get object that will be instanced
    objectlist = cmds.ls(selection = True, dagObjects = True , exactType = "mesh")
    object = objectlist[0]
    
    #Optional parameter that randomizes component placement
    if PlacementAmountFactor != 1:
        PlacementAmount = int((len(components)) * (PlacementAmountFactor)) 
        components = random.sample(components, k = PlacementAmount)
    
    #iterate over each vertex, creating rivet and instance
    instanceGroupName=cmds.group(empty=True, name=object + "_instance_grp#")
    
    for component in components:
        cmds.select(deselect = True)
        currentInstance = cmds.instance(object, name = object + "_instance#")
        cmds.parent(currentInstance, instanceGroupName)
        cmds.select(component, currentInstance , add = True)
        cmds.pointOnPolyConstraint(component, currentInstance, offset = [Xoffsetamount, Yoffsetamount, Zoffsetamount], weight = weightAmount)
        # calls function to randoimize instance if requested
        instanceRandomizer(currentInstance, RotationRange, ScaleRangeEnd, ScaleRangeStart, PlacementAmountFactor)

# Optional settings to randomize instances
def instanceRandomizer(currentInstance, RotationRange, ScaleRangeEnd, ScaleRangeStart, PlacementAmountFactor, *pArgs):
    
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
def UI(instanceIteration):
    
    windowID = 'myWindowID'
    global windowID
    if cmds.window( windowID, exists=True ):
        cmds.deleteUI( windowID )
    
    win = cmds.window( windowID, title = "PointonPolyConstraintInstancer", sizeable = False, resizeToFitChildren = True)

    cmds.rowColumnLayout(numberOfColumns = 4)
    
    cmds.separator( width=1, style='none' )
    cmds.text(label = "Random Rotation Range:", align = "right")
    cmds.separator( w=1, style='none' )
    RotationRangeField = cmds.floatFieldGrp( numberOfFields=3, value1 = 0, value2 = 0, value3 = 0)
   
    cmds.separator( w=1, style='none' )
    cmds.text(label = "Random Scale Range Start Values:", align = "right")
    cmds.separator( width=1, style='none' )
    ScaleRangeStartField = cmds.floatFieldGrp( numberOfFields=3, value1 = 1, value2 = 1, value3 = 1 )
    
    cmds.separator( w=1, style='none' )
    cmds.text(label = "Random Scale Range End Values:", align = "right")
    cmds.separator( width=1, style='none' )
    ScaleRangeEndField = cmds.floatFieldGrp( numberOfFields=3, value1 = 1, value2 = 1, value3 = 1 )
    
    cmds.separator( w=1, style='none' )
    cmds.text(label = "Random Component Placement Value:", align = "right")
    cmds.separator( width=1, style='none' )
    PlacementAmountField = cmds.floatField(value = 1, minValue = 0, maxValue = 1) 
    
    cmds.separator( w=1, style='none' )
    cmds.text(label = "Offset", align = "right")
    cmds.separator( width=1, style='none' )
    OffsetField = cmds.floatFieldGrp( numberOfFields=3, value1 = 0, value2 = 0, value3 = 0)
        
    cmds.separator( w=1, style='none' )
    cmds.text(label = "Weight", align = "right")
    cmds.separator( width=1, style='none' )
    WeightField = cmds.floatSliderGrp( field = True, min = 0, max = 1, value = 1) 
    
    cmds.separator( h=20, style='none' )
    cmds.separator( h=20, style='none' )
    cmds.separator( h=20, style='none' )
    cmds.separator( h=20, style='none' )

    cmds.separator( w=1, style='none' )
    cmds.separator( w=1, style='none' )
    
    cmds.button(label="Apply", command=functools.partial(instanceIteration, RotationRangeField, 
                                                         ScaleRangeEndField, ScaleRangeStartField, 
                                                         PlacementAmountField, OffsetField, WeightField)) 
    cmds.button(label="Cancel", command = CloseUI)
    
    cmds.showWindow(win)

def CloseUI(*pArgs):
     if cmds.window( windowID, exists=True ):
        cmds.deleteUI( windowID )

UI(instanceIteration)