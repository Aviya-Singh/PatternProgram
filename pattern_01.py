pattern=input("Enter the string: ")
lenpattern=len(pattern)
#print(lenpattern)
for row in range(lenpattern):
    for col in range(row+1):
        print(pattern[col],end="")
    print()