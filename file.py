f1 = open('india.txt','r')
f2 = open('new_india.txt','w+')

for line in f1.readlines():
    f2.write(line)

f1.close()
f2.close()

f2 = open('new_india.txt','r')
print(f2.read())



