import math
#This file will create simulcrypt ECMG connections.
#The System IDs in KMS.
systemIds= [1572,1536]
#The id of KMS network.
networkId= 18
#The IP addresses of SCS.
hosts = ["10.86.16.186"]
#The number of services each SCS.
serviceNumber = 2
#The total number of transport.
numberOfTS =16
#The start ID of transport.
startTSID=4
for host in hosts: 
  port = 4350 for transport in range(startTSID,startTSID+numberOfTS):  
    for systemId in systemIds:    
      i=1   services=''   
      print(transport)   
      print("\n")   
      fp=open("C:\Files\SCS_"+str(host)+"_"+str(systemId)+"_Port"+str(port)+"_TS"+str(transport)+".bat",'a')   
      while(i<serviceNumber):    
        services= services+" --serviceid "+str((transport-4)*40+i+3)
        # For each TS have 43 or 40 products in 21M performance DB.    
        print(services)    
        i+=1   
        fp.write("start \"ECM "+str(port)+":transportid "+str(port)+" systemid "+str(systemId)+"\" "+"SCS.exe --host "+str(host)+" --port "+str(port)+" --systemid "+str(systemId)+" --networkid "+str(networkId)+" --transportid "+str(transport)+services+'\n')   
        port +=1  
        fp.flush() 
        fp.close()
