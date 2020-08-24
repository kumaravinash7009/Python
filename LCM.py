def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b)

a,b = input().split()

LCM = (int(a)*int(b))/ gcd(int(a), int(b))
 
print (int(LCM))
