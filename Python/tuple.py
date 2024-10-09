tup=(4,4.56,"Hi","Hello",[3,"Hey"],True,"Hi")

print(tup[2])
print(tup[-3::1])

print(tup.index("Hello"))
print(tup.count("Hi"))
l1=list(tup)
l1.append("good")
tup1=tuple(l1)
l2=list(tup1)
l2.remove("good")
print(tuple(l2))
setA={1,4,4.56,"Hi","Hello",True,"Hi"}
setB={2,4.57,1,"Hello","Hi",True}
print(setA|setB)
print(setA&setB)
print(setA^setB)

print(setA-setB)
l=[1,23,334,5.6,"hi",1,1,2,334,"hi"]
l=set(l)
print(l)
l.add("spring")
print(l)

l.remove('hi')
print(l)
