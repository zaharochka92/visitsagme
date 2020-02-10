words=[]
with open('words.txt', 'r') as f:
    for i in range(0,500):
        a=f.readline()
        words.append(a[0:len(a)-1])

print(words)