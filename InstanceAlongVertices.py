import maya.cmds as cmds

#get all the components to instance over
#set variable to allow user to pick which component type through UI
def componentSelection(componentType = "Faces"):
    if componentType = "Edges":
        components = cmds.filterExpand(selectionMask = 32)
    elif componentType = "Faces":
        components = cmds.filterExpand(selectionMask = 34)
    elif componentType = "Vertices"
        components = cmds.filterExpand(selectionMask = 31)
    return components
#main function that perfoms the actual processes
def instanceIteration():
    
    #get object that will be instanced
    objectlist = cmds.ls(selection = True, dagObjects = True , exactType = "mesh")
    object = objectlist[0]
    
    #get components to be iterated over
    components = componentSelection()
    
    #iterate over each vertex, creating rivet and instance
    instanceGroupName=cmds.group(empty=True, name=object + "_instance_grp#")
    instancedict=dict()
    
    for component in components:
        cmds.select(deselect = True)
        instancedict[component] = cmds.instance(object,name=object + "_instance#" , smartTransform = False)
        cmds.parent(instancedict[component],instanceGroupName)
        cmds.select(component, instancedict[component] , add = True)
        cmds.pointOnPolyConstraint(component, instancedict[component])

#Create UI for script
def UI():
    global windowID
    windowID = 'myWindowID'
    
    if cmds.window( windowID, exists=True ):
        cmds.deleteUI( windowID )
    cmds.window( windowID, title = "PointonPolyConstraintInstancer", sizeable=False, resizeToFitChildren=True )
    cmds.rowColumnLayout(numberOfColumns = 2)
    

    
    cmds.button(label="Apply",command = "changeNames(objectList)")
    
    cmds.showWindow()
   