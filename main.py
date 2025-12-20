#program to draw a right angled triangle
print("------RIGHT-ANGLED TRIANGLE------")
n=int(input("Enter the number of rows: "))
#outer loop-content of the pattern
for i in range(n):
    #inner loop content of the pattern
    for j in range(i+1):
        #print content
        print("*",end="")
    #new line after each row
    print()