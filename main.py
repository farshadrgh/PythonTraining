print("Printing current and previous number sum in a given range(10)")
previous_Number = 0
sum = 0
for num in range (1 ,11):
    print("Current Number {} Previous Number {}  Sum: {}".format(num-1, previous_Number, sum))
    previous_Number = num -1
    sum =num + previous_Number
