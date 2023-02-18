import os
import socket
from collections import Counter

Counter = Counter()

wc = {}
path ="/home/data"
if os.path.exists(path + "/" +"result.txt"):
  os.remove(path + "/" +"result.txt")
outStr="****|| text file at location: /home/data ||****\n"

def wordCount(file):
    ttlWrdCnt = 0
    with open(file, 'r') as file:
        for line in file:
            if (line != '\n'):
                if (file.name.endswith("IF.txt")):
                    Counter.update(line.replace("Â", "").split())
                ttlWrdCnt = ttlWrdCnt + len(line.replace("Â", "").split())
    return ttlWrdCnt

for eachFile in os.listdir(path):
    if eachFile.endswith(".txt"):
        outStr=outStr+eachFile+"\n"
        wc[eachFile] = wordCount(path + "/" + eachFile)
		
outStr=outStr+"\n"
outStr=outStr+"****|| b.Read the two text files and total the amount of words in each. ||****\n"
FileWc = 0
FileNames = ""
for eachkey in wc.keys():
    FileNames = FileNames + eachkey + ","
    FileWc = FileWc + wc.get(eachkey)
    outStr = outStr +"total amount of words included in [" + eachkey + "] is : " + str(wc.get(eachkey))+"\n"

outStr = outStr +"\n"
outStr = outStr +"****|| total (the total number of words in both files)) ||****\n"
outStr = outStr +"total word count in both files [" + FileNames[0:len(FileNames) - 1] + "] is: " + str(FileWc)+"\n"

outStr = outStr +"\n"
outStr = outStr +"****|| top three words with the most counts in IF.txt ||****\n"
outStr = outStr +str(Counter.most_common(3))+"\n"

outStr = outStr +"\n"
outStr = outStr +"****|| IP address ||****\n"
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
outStr = outStr +"Your Computer IP Address is:" + IPAddr

res = open(path + "/" +"result.txt","w")
res.write(outStr)
res.close()
for eachline in open(path + "/" +"result.txt","r").readlines():
    print(eachline.replace("\n",""))