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
       counts[word]=counts.get(word,0)+1
rst=list()
for key,val in list(counts.items()):
  rst.append((val,key))
rst.sort(reverse=True)
print("10 Most Common Words are: ")
for i in rst[:10]:
    print("%d  %s" %i)
delayy(8000)