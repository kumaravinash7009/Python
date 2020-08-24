def lcm(a, b):
   if a > b:
       bigger = a
   else:
       bigger = b

   while(True):
       if bigger % a == 0 and bigger % b == 0:
           lcm = bigger
           break
       bigger += 1

   return lcm

a=int(input("Enter your first no.: "))  
b=int(input("Enter your second no.: "))  

print ("The LCM is : ",end="") 
print (lcm(a,b))
