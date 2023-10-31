pattern=input("Enter the string: ")
lenpattern=len(pattern)
#print(lenpattern)
for row in range(lenpattern, 0, -1):
    for col in range(0,row):
        print(pattern[col],end="")
    print()