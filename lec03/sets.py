#Create an empty set
s = set()

#Add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
for i in range(5, 50):
    s.add(i)

print(s)
print(f"The set has {len(s)} elements")

for i in range(1,50,2):
    s.remove(i)
print(s)