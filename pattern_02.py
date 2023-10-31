userInput=int(input("Enter the pattern to be printed: "))
for row in range(userInput,0,-1):
    for col in range(1,row+1):
        print(col,end="")
    print()

#54321
#5432
#543
#54
#5