sum = 0
total = 0
b = 1
count = 0
done = False
while b < 5 and done!= True:
    number = int(input("Enter number {}".format(b)))
    sum = sum  + number
    count = count + 1

    b = b + 1

    if b == 12:
        done = True
        break

print("The mean of these numbers is {}".format(sum/count))
