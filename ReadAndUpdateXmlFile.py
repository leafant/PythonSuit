def updateCcaSlotInScdFile(self, fileName = '', slot = '',  indexOf3AesPesk = '', newSn = False):    
    '''    Will update values of slot, sn, ua in specified scd file. Only one card  exist in the file.    Since we can't upload duplicated sn in Db, so the method will also update sn and ua when change the value of Slot.    '''    
    if "\\" not in fileName:        
        rootFolder = Cfg.getConfigurationItem('AppServer.TestRoot')        
        fileName =  os.path.join(rootFolder,  'DataFiles', fileName)    
    tree = ElementTree()    tree.parse(fileName)    
    root = tree.getroot()             
    nodes = root.findall("PROFILE/CLIENT_DEVICE_DATA/GLOBAL_PK")        
    ## Update the slot and index value. Only 3aes Pesk support Pesk.    
    for node in nodes:        
        print node.get("slot")        
        if(node.get("slot") != None):            
        node.set("slot", slot)            
        if(indexOf3AesPesk != ''):                
            indexNode = node.findall("INDEX")                
            indexNode[0].text = indexOf3AesPesk
    tree.write(fileName, encoding="utf-8")
