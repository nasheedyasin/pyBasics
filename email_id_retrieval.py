def delayy(n):
    i=0
    while i<n:
        j=0
        while j<n:
            j+=1
        i+=1

import urllib.request
name=input("Enter the Name of the text file: ")
fhand= urllib.request.urlopen("http://data.pr4e.org/"+name+".txt")

counts=dict()
for line in fhand:
    words=line.decode().split()
    for word in words:
        if word.find("@") == -1:
            continue
        counts[word]=counts.get(word,0)+1
    

for key,val in list(counts.items()):
    print(key,val)  
delayy(8000)