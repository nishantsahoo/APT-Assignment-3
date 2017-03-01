import os
print("1. Q1  \n2. Q2  \n3. Q3  \n4. Q4  \n5. Q5\n")
choice = int(input("Enter the desired choice: "))
if choice not in range(1,6):
    print("Wrong choice")
else:
    os.system("python Q" + str(choice) + ".py")
