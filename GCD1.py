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


 
    