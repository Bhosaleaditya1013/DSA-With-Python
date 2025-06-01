l1= [[1,2,3],[4,5,6],[7,8,9]]
l2= [[1,2,3],[4,5,6],[7,8,9]]

print("L1: ")
for row in range(0,3):
    for col in range(0,3):
        print(l1[row][col],end=" ")
    print()
    
print("L2: ")
for row in range(0,3):
    for col in range(0,3):
        print(l2[row][col],end=" ")
    print()
    
print("Addition of two matrics: L1+L2:")

for row in range(0,3):
    for col in range(0,3):
        print(l1[row][col]+l2[row][col],end=" ")
    print()
    
    