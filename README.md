# CMPSCI-132-Project
#Master file contains the most current scripts that will be used.

#Object Renamer renames objects according to a set convention based on their distance to each other, this is useful in creating matching low and high poly assets for game art production.

  Explanation: 
    The script scans the user's selected objects. It will match pairs of objects that are closest together. Then rename them accordingly.  Additionally it will identify which object has more polygons and associate it with other objects in the other pairs that are higher in polygons. So now we have pairs of objects that are overlapping and two sets of objects based on polys. Objects in the same pair have the same base name, however objects in the high poly set have _high as suffix and objects in low poly have _low.  
    
    The point of this script is to help rename objects for texture baking. http://wiki.polycount.com/wiki/Texture_Baking

#Branch 1 is just smaller scripts used in the master files, mainly kept for reference. 
