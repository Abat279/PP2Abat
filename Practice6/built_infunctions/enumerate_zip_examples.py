
names = ["Ali","Dana","Aruzhan"]

for i,name in enumerate(names):
    print(i,name)



for i,name in enumerate(names,start=1):
    print(i,name)



scores = [90,85,88]

for name,score in zip(names,scores):
    print(name,score)



pairs = list(zip(names,scores))
print(pairs)



ages = [20,21,22]

for n,s,a in zip(names,scores,ages):
    print(n,s,a)