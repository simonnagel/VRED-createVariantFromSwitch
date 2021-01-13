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

def variantRenderPreview(varSetName):
    mats = getMaterialVariants(varSetName)
    mat = findMaterial(mats[0])
    nodes = mat.getNodes()  
    selectNode(nodes[0])  
    zoomTo(nodes[0])
    setIsolateView(-1,nodes)
    selectVariantSet(varSetName)
    renderVariantSetPreview(varSetName)
    resetIsolateView(-1)
    print("variantPreviewRendered"+varSetName)

def createVariantFromMaterialSwitches(choice,override):       
    if choice == "all":    
        allMats = getAllMaterials()
    elif choice == "selected":
        allMats = getSelectedMaterials()
        
    if override == "override":
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
        switchMatName = switchMat.getName()    
        switchMatChildren = switchMat.getSubMaterials()
        switchMatChildrenName = switchMat.getName()    
        numberChildren = len(switchMatChildren)        
        varGroup = createVariantSetGroup("___M_"+switchMatName)
               
        for i in range(0,numberChildren):
            child = switchMatChildren[i].getName()       
            varSetName = "M_"+child
            varSet = createVariantSet(varSetName)       
            moveVariantSetToGroup(varSetName,"___M_"+switchMatName) 
            varSet.addMaterial(switchMat,child)
            variantRenderPreview(varSetName)

 
                                               
createVariantFromMaterialSwitches("all","override")

#variantRenderPreview("M_Metallic black")
