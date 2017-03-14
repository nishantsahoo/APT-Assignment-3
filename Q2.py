l1 = input("Enter the first expression: ")
l2 = input("Enter the second expression: ")
l1_list = l1.split('+')
l2_list = l2.split('+')
result = []

for i in range(0, 3):
    l1_list[i] = (l1_list[i].strip())[:-1]
for i in range(0, 3):
    l2_list[i] = (l2_list[i].strip())[:-1]
for i in range(0, 3):
    result.append(str((int(l1_list[i])+int(l2_list[i]))))
for i in range(0, 3):
    result[i] += chr((ord("x")+i))
answer = " + ".join(result)
print(answer)
