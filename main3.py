#program to draw a mirrored right angled triangle
n=int(input("Enter the number of rows: "))
print("------MIRRORED RIGHT-ANGLED TRIANGLE------")
#outer loop-content of the pattern
for i in range(n):
    #inner loop-space of the pattern
    for j in range(n-i-1):
        #print space
        print(" ",end="")
    #inner loop content of the pattern
    for k in range(i+1):
        #print content
        print("*",end="")
    #new line after each row
    print()