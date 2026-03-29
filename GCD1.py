#this class job is to find the greatest common diviser of 2 ints
#using the euclidean algorthim 
class GCD:
    

    #starting the function and calling it 
    def find_GCD(self , a, b):
        self.a = a
        self.b = b
    
    
        #Keep going until there is no remainder left
        while b != 0:
            #Find the remainder when a is divided
            rem = a % b
            #Move b into a, and the remainder into b 
            a = b
            b = rem
            #when b reaches 0, a is the answer (the GCD)
        return a
while True:
    #take the input from the user for the first number
    num1 = input('Enter your first number')
    #take the input from the user for the second number
    num2 = input('Enter your second number')
    #checking if both numbers are digits
    if num1.isdigit() and num2.isdigit():
        #conversting strings into integers
        num1 = int(num1)
        num2 = int(num2)
        #check if both numbers are positive
        if num1 > 0 and num2 > 0:
            #create an object GCD
            x = GCD()
            #call the function to find the GCD for the 2 numbers
            result = x.find_GCD(num1, num2)
            print(f'GCD {result}')
            break
            
        else:
            #print an error if any number is zero or negitive
            print('the number must be positive')
    else:
        #print an error message if the input has no digital characters
        print('the number is invalid')


 