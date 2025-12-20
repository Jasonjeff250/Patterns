#floyd's triangle-number triangle
print("------FLOYD'S TRIANGLE------")
rows=int(input("Enter the number of rows: "))
#increase the numbers
number=1
#outer loop-number of rows
for i in range(1,rows+1):
    #inner loop-numbers in each row
    for j in range(1,i+1):
        #print the number
        print(number,end=" ")
        #increment the number
        number+=1
    #print blank line
    print()