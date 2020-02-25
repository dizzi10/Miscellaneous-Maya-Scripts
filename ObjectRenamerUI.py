import maya.cmds as cmds
import functools

def UI():
    windowID = 'myWindowID'
    if cmds.window( windowID, exists=True ):
        cmds.deleteUI( windowID )
    cmds.window( windowID, title = "ObjectRenamer", sizeable=False, resizeToFitChildren=True )
    cmds.rowColumnLayout(numberOfColumns = 2)
    cmds.showWindow()
UI()