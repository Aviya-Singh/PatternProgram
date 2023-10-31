userInput=input("Enter the string: ")
length=len(userInput)
print(length)
for row in range(length,0,-1):
    for col in range(1,row+1):
        print(userInput[col],end="")
    print()