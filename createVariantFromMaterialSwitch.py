'''
DISCLAIMER:
---------------------------------
In any case, all binaries, configuration code, templates and snippets of this solution are of "work in progress" character.
This also applies to GitHub "Release" versions.
Neither Simon Nagel, nor Autodesk represents that these samples are reliable, accurate, complete, or otherwise valid. 
Accordingly, those configuration samples are provided “as is” with no warranty of any kind and you use the applications at your own risk.
Scripted by Simon Nagel
How to use:
Paste in your VRED Script Editor and Execute
Execute the Variant with the ending *_blend to blend into that Variant Set
Scripted by Simon Nagel
'''

def deleteVariantForMaterialSwitches():
    allVarSets = getGroupedVariantSets()
    for i in allVarSets:
        varSetsInOneGroup = allVarSets[i]
        varGroupName= str(i)
        if varGroupName[:5] =="___M_":
            deleteVariantSetGroup(str(varGroupName))
        for j in varSetsInOneGroup:
            varSetName = str(j)
            if varSetName[:2] =="M_":
                deleteVariantSet(varSetName)
    print ("All VariantGroups starting with '___M_' were deleted")
    print ("All Variants starting with 'M_' were deleted")

def variantMaterialRenderPreview(varSetName,node,autoZoom):
    if autoZoom == "true":
        zoomTo(node)
    selectVariantSet(varSetName)
    renderVariantSetPreview(varSetName)      
    print("variantPreviewRendered"+varSetName)

def createVariantFromMaterialSwitches(choice,override,preview,autoZoom):
    camPos = findNode("Perspective").getTranslation()
    camRot = findNode("Perspective").getRotation()     
    if choice == "all":    
        allMats = getAllMaterials()
    elif choice == "selected":
        allMats = getSelectedMaterials()
        
    if override == "true":
        deleteVariantForMaterialSwitches()    
    switchMats = []
    del switchMats[:]
    
    for j in range(0,len(allMats)):        
        tempMat = allMats[j]
        matTpye = tempMat.getType()    
        if matTpye == "SwitchMaterial":
            switchMats.append(tempMat)
                
    for j in range(0,len(switchMats)):
        
        switchMat = switchMats[j]
        switchMatNodes = switchMat.getNodes() 
        switchMatNode = switchMatNodes[0]
        origSwitchMatChoice= switchMat.getChoice()
        switchMatName = switchMat.getName()    
        switchMatChildren = switchMat.getSubMaterials()
        switchMatChildrenName = switchMat.getName()    
        numberChildren = len(switchMatChildren)        
        varGroup = createVariantSetGroup("___M_"+switchMatName)
               
        for i in range(0,numberChildren):
            child = switchMatChildren[i].getName()       
            varSetName = "M_"+child
            deleteVariantSet(varSetName)
            varSet = createVariantSet(varSetName)       
            moveVariantSetToGroup(varSetName,"___M_"+switchMatName) 
            varSet.addMaterial(switchMat,child)
            if preview == "true":
                variantMaterialRenderPreview(varSetName,switchMatNode,autoZoom)
        switchMat.setChoice(origSwitchMatChoice)
    findNode("Perspective").setTranslation(camPos[0],camPos[1],camPos[2])
    findNode("Perspective").setRotation(camRot[0],camRot[1],camRot[2])   

 
                                               
#createVariantFromMaterialSwitches("all","true","true","true")
createVariantFromMaterialSwitches("selected","false","true","false")

print ("node")

