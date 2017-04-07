        f1 = open('C:\Sublines\DataFiles\*.osc', 'r')            
        lines = f1.read()        r = r"<KEY KEYINDEX=\"0\">.*<\/KEY>"        
        replace = re.sub(r, '<KEY KEYINDEX="0">1111114B4145534B45592215441554B4</KEY>', lines)        
        f1.close()        
        f2 = open('C:\Sublines\DataFiles\*.osc', 'a')        
        f2.write(replace)        
        f2.close()
