# Miscellaneous-Maya-Scripts

#Object Renamer renames objects according to a set convention based on their distance to each other, this is useful in creating matching low and high poly assets for game art production.

  Explanation: 
    The script scans the user's selected objects. It will match pairs of objects that are closest together. Then rename them accordingly.  Additionally it will identify which object has more polygons and associate it with other objects in the other pairs that are higher in polygons. So now we have pairs of objects that are overlapping and two sets of objects based on polys. Objects in the same pair have the same base name, however objects in the high poly set have _high as suffix and objects in low poly have _low.  
    
    The point of this script is to help rename objects for texture baking. http://wiki.polycount.com/wiki/Texture_Baking

To demo the scripts you need to install the software
Download any version of maya, You can get a free license by applying as a student.
Link: https://www.autodesk.com/education/free-software/maya

Once downloaded, use maya to open the finaliteration.0001.ma file included in this folder.

Go to the bottom of the maya ui and open the script editor, it should be a small icon in the botom right corner 

Go to file in the script editor then open each script included in this file.

To run a script you need to highlight the code then click the blue arrows in the script editor

Object Renamer:
1.) Select an even amount of objects.
2.) Make sure the corresponding objects overlap.
3.) Execute the script.
4.) Open the object outliner by clicking the icon on the left side of the maya ui.
5.) Here you can see the results of the script and double check they are named properly

Point on Poly Constraint Instancer:
1.) Click the object you want to instance on. Then hold right click to select the desired component type. Shift click as many you want.
2.) Then shift click the object to be instanced.
3.) Run the script and adjust the parameters as desired. 

Duplicate Along Curve with Mash V2:
1.) Select the curve given in the scene or create your own using the create tap on the top of the maya window, if creating your own curve go to curve tools then Cv curve tool and click on the scene to draw your curve.
2.) Run the script, choose autofill to have your object fill the curve or manual mode to pick how many times you want it on there.

Note:
Maya is a buggy software. If something does not work try opening a new scene or restarting.
If problem persists, try:
1.) Go to edit => delete all by type => history
2.) Select your objects then Modify => Freeze Transformations
3.) Select your objects then Modify => center pivot then bake pivot
4.) The point on poly constraint instancer will not work if the object has overlapping uvs, I suggest you to only use the demo tire to test that, if not you can google how to get uvs using automatic projection and then laying them out to avoid overlapping in the uv editor
