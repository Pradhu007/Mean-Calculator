sum = 0 #Keeps updating the values of the numbers entered
start = 0 #Indicates the start of the loop
end = 5 #You can change this value depending on the amount of numbers you want to calculate to get the mean.
#For example, say if you want to find the mean of 5 numbers(by default), you change the end variable to hold the value 5 .  
count = 0
done = False
while start < end and done!= True:
    number = int(input("Enter number {}".format(b)))
    sum = sum  + number #Adds numbers to the sum variable as numbers are inputted 
    count = count + 1#Keeps track of the count of numbers that were inputted

    start = start + 1 #Increments the control variable "start"

    if start == end:
        done = True
        break #This statement which terminates the loop. 

total = sum/count
print("The mean of these numbers is {}".format(total))

#Credits:Pradhu007
