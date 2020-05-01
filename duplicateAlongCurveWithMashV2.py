import maya.cmds as cmds
import MASH.api as mapi
import mash_repro_utils as repro
import mash_repro_aetemplate as AErepro
import functools


def createMashNetwork(node, node2, transformNode):
    
    # create a new MASH network
    mashNetwork = mapi.Network()
    mashNetwork.createNetwork(name = "MASH")
   
    # connect object to repro node for instancing
    repro.connect_mesh_group('MASH_Repro', node) 
    AErepro.refresh_all_aetemplates() # Refresh the attribute editor for all repro nodes
    
    #change attribute on distribute node to make object follow curve
    #cmds.setAttr( 'MASH_Distribute.arrangement', 7 )
    cmds.setAttr( 'MASH_Distribute.amplitudeX', 0 )
 
    #Create Curve Node with Curve
    Curvenode = mashNetwork.addNode("MASH_Curve")
    
    #change curve node attribute to having object duplicate around entire curve 
    cmds.setAttr("MASH_Curve.timeStep", 1)
    bug = "MASH_Curve"
    cmds.connectAttr(node2[0] + '.worldSpace[0]', bug + ".inCurves[0]", force=1)
    
    cmds.showHidden( node2 )
    cmds.showHidden( transformNode )
          
    
#this function finds the number of points needed to fill curve
def addpoints(node,node2):
    
    curvelen = (cmds.arclen(node2))
    #need bbbox
    #use that to drive number of points in curve node according to arclen
    bbox = cmds.exactWorldBoundingBox(node)
    objlen = (bbox[3]- bbox[0])
    numpoints = int(curvelen//objlen)
    cmds.setAttr( 'MASH_Distribute.pointCount', numpoints )

#get objects used in script   
def Main(node, node2, transformNode, pointsAmount, pointCheck, *pArgs):
    
    #run function that creates mash network
    createMashNetwork(node, node2, transformNode)
    
    #using inputs fromm UI
    valueCheck = [None, True, False]
    #returns a value showing which button is checked
    pointCheckValue = cmds.radioButtonGrp(pointCheck, query = True, select = True)
    if valueCheck[pointCheckValue] == False or valueCheck[pointCheckValue] == None:
        #add points to mash for autofill curve option
        addpoints(node,node2)
        #runs the addpoints function everytime arclen is changed to update number of points
        curveInfoNode = cmds.arclen(node2, ch=True) #creates node that tracks arclen of curve
        cmds.scriptJob(attributeChange=["curveInfo1.arcLength", "addpoints(node,node2)"])
        cmds.scriptJob(attributeChange=[transformNode[0]+".scaleX", "addpoints(node,node2)"])
        
        
    else:
        #add points to mash for manual option
        points = cmds.intField(pointsAmount, value = True, query = True)
        cmds.setAttr( 'MASH_Distribute.pointCount', points )

def UI(Main, node, node2, transformNode):
    global windowID
    windowID = 'myWindowID'

    if cmds.window(windowID, exists=True):
        cmds.deleteUI(windowID)
        
    cmds.window(windowID, title="duplicateAlongCurve", sizeable=False)
    cmds.rowColumnLayout(numberOfColumns=1)
    cmds.separator(style = 'none')

    
    
    pointCheck = cmds.radioButtonGrp( label='Amount of Points', columnAlign=[1,"left"], labelArray2=['Manual', 'AutoFillCurve'], numberOfRadioButtons=2 )
    cmds.text(label = "Number of Points (Only for Manual mode)", align = "left")
    pointsAmount = cmds.intField(value = 0)
    cmds.separator(style = 'none')
    cmds.button(label="Apply", command=functools.partial(Main, node, node2, transformNode, pointsAmount, pointCheck ))
    
    def deleteWindow(*pArgs):
        if cmds.window(windowID, exists=True):
            cmds.deleteUI(windowID)  
            
    cmds.button(label="Cancel", command=deleteWindow)
    cmds.showWindow()

    #cmds.deleteUI(windowID)

#get object
objectlist = cmds.ls(selection = True, dagObjects = True , exactType = "mesh")
node = objectlist[0]

#get object's transform node to be used in scriptjob
transformNode = cmds.listRelatives(node, parent=True, fullPath=True)

#get curve 
node2 = cmds.filterExpand(selectionMask = [9,11])
      
UI(Main, node, node2, transformNode)



